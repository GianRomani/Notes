var suggestions = document.getElementById('suggestions');
var userinput = document.getElementById('userinput');

if (suggestions && userinput) {
  document.addEventListener('keydown', inputFocus);

  function inputFocus(e) {
    const isCmdK = (e.metaKey || e.ctrlKey) && e.keyCode === 75;
    const isForwardSlash = e.keyCode === 191;

    if ((isCmdK || isForwardSlash)
        && document.activeElement.tagName !== "INPUT"
        && document.activeElement.tagName !== "TEXTAREA") {
      e.preventDefault();
      userinput.focus();
    }

    if (e.keyCode === 27 ) { // Escape key to close suggestions
      userinput.blur();
      suggestions.classList.add('d-none');
      document.body.classList.remove('command-palette-open');
    }
  }

  // Hide suggestions when clicking outside
  document.addEventListener('click', function(event) {
    var isClickInsideSuggestions = suggestions.contains(event.target);
    var isClickInput = (event.target === userinput);

    if (!isClickInsideSuggestions && !isClickInput) {
      suggestions.classList.add('d-none');
      document.body.classList.remove('command-palette-open');
    }
  });

  // Handle keyboard navigation inside search suggestions
  document.addEventListener('keydown', suggestionFocus);

  function suggestionFocus(e) {
    const focusableSuggestions = suggestions.querySelectorAll('.suggestion-link');
    if (suggestions.classList.contains('d-none') || focusableSuggestions.length === 0) {
      return;
    }
    const focusable = [...focusableSuggestions];
    const index = focusable.indexOf(document.activeElement);

    if (e.keyCode === 38) { // Up arrow
      e.preventDefault();
      if (index === 0) {
        userinput.focus();
      } else if (index > 0) {
        focusableSuggestions[index - 1].focus();
      }
    }
    else if (e.keyCode === 40) { // Down arrow
      e.preventDefault();
      if (index === -1) {
        focusableSuggestions[0].focus();
      } else if (index + 1 < focusable.length) {
        focusableSuggestions[index + 1].focus();
      }
    }
  }

  // Initialize elasticlunr search execution
  (function(){
    if (!window.searchIndex) {
      console.warn("Search index not found");
      return;
    }
    var index = elasticlunr.Index.load(window.searchIndex);
    
    userinput.addEventListener('input', show_results, true);
    userinput.addEventListener('focus', function() {
      document.body.classList.add('command-palette-open');
      if (this.value.trim().length > 0) {
        show_results.call(this);
      }
    });
    userinput.addEventListener('click', function() {
      document.body.classList.add('command-palette-open');
      if (this.value.trim().length > 0) {
        show_results.call(this);
      }
    });
    
    suggestions.addEventListener('click', accept_suggestion, true);
    
    function show_results() {
      var value = this.value.trim();
      suggestions.innerHTML = ''; // Safely clear all old suggestions

      if (value.length === 0) {
        suggestions.classList.add('d-none');
        return;
      }

      var options = {
        bool: "OR",
        fields: {
          title: {boost: 2, expand: true},
          body: {boost: 1, expand: true},
          expand: true
        }
      };
      var results = index.search(value, options);
      suggestions.classList.remove('d-none');

      // Filter pages that have content/body to show
      var validResults = results.filter(function(page) {
        return page.doc.body && page.doc.body.trim() !== '';
      });

      if (validResults.length === 0) {
        var noResults = document.createElement('div');
        noResults.className = 'suggestion-no-results';
        noResults.innerHTML = 'No results found for "<span>' + escapeHTML(value) + '</span>"';
        suggestions.appendChild(noResults);
        return;
      }

      var items = value.split(/\s+/);
      var maxResults = Math.min(validResults.length, 6);

      for (var i = 0; i < maxResults; i++) {
        var page = validResults[i];
        var entry = document.createElement('div');
        entry.className = 'suggestion-item';

        var a = document.createElement('a');
        a.href = page.ref;
        a.className = 'suggestion-link';

        var title = document.createElement('div');
        title.className = 'suggestion-title';
        title.textContent = page.doc.title;

        var teaser = document.createElement('div');
        teaser.className = 'suggestion-teaser';
        teaser.innerHTML = makeTeaser(page.doc.body, items);

        a.appendChild(title);
        a.appendChild(teaser);
        entry.appendChild(a);
        suggestions.appendChild(entry);
      }
    }

    function accept_suggestion() {
      suggestions.innerHTML = '';
      suggestions.classList.add('d-none');
    }

    // Snippet extraction with search highlights
    function makeTeaser(body, terms) {
      var TERM_WEIGHT = 40;
      var NORMAL_WORD_WEIGHT = 2;
      var FIRST_WORD_WEIGHT = 8;
      var TEASER_MAX_WORDS = 20;
    
      var stemmedTerms = terms.map(function (w) {
        return elasticlunr.stemmer(w.toLowerCase());
      });
      var termFound = false;
      var index = 0;
      var weighted = []; // contains elements of ["word", weight, index_in_document]
    
      // split in sentences, then words
      var sentences = body.toLowerCase().split(". ");
      for (var i in sentences) {
        var words = sentences[i].split(/[\s\n]/);
        var value = FIRST_WORD_WEIGHT;
        for (var j in words) {
          var word = words[j];
          if (word.length > 0) {
            for (var k in stemmedTerms) {
              if (elasticlunr.stemmer(word).startsWith(stemmedTerms[k])) {
                value = TERM_WEIGHT;
                termFound = true;
              }
            }
            weighted.push([word, value, index]);
            value = NORMAL_WORD_WEIGHT;
          }
          index += word.length;
          index += 1;
        }
        index += 1;
      }
    
      if (weighted.length === 0) {
        if (body.length !== undefined && body.length > TEASER_MAX_WORDS * 10) {
          return escapeHTML(body.substring(0, TEASER_MAX_WORDS * 10)) + '...';
        } else {
          return escapeHTML(body);
        }
      }
    
      var windowWeights = [];
      var windowSize = Math.min(weighted.length, TEASER_MAX_WORDS);
      var curSum = 0;
      for (var i = 0; i < windowSize; i++) {
        curSum += weighted[i][1];
      }
      windowWeights.push(curSum);
    
      for (var i = 0; i < weighted.length - windowSize; i++) {
        curSum -= weighted[i][1];
        curSum += weighted[i + windowSize][1];
        windowWeights.push(curSum);
      }
    
      var maxSumIndex = 0;
      if (termFound) {
        var maxFound = 0;
        for (var i = windowWeights.length - 1; i >= 0; i--) {
          if (windowWeights[i] > maxFound) {
            maxFound = windowWeights[i];
            maxSumIndex = i;
          }
        }
      }
    
      var teaser = [];
      var startIndex = weighted[maxSumIndex][2];
      for (var i = maxSumIndex; i < maxSumIndex + windowSize; i++) {
        var word = weighted[i];
        if (startIndex < word[2]) {
          teaser.push(escapeHTML(body.substring(startIndex, word[2])));
          startIndex = word[2];
        }
    
        if (word[1] === TERM_WEIGHT) {
          teaser.push("<mark class='search-highlight'>");
        }
  
        startIndex = word[2] + word[0].length;
        var re = /^[\x00-\xff]+$/;
        if (word[1] !== TERM_WEIGHT && word[0].length >= 12 && !re.test(word[0])) {
          var strBefor = body.substring(word[2], startIndex);
          var strAfter = substringByByte(strBefor, 12);
          teaser.push(escapeHTML(strAfter));
        } else {
          teaser.push(escapeHTML(body.substring(word[2], startIndex)));
        }
    
        if (word[1] === TERM_WEIGHT) {
          teaser.push("</mark>");
        }
      }
      teaser.push("…");
      return teaser.join("");
    }
  }());
}

// Helper to escape HTML characters safely
function escapeHTML(str) {
  return str.replace(/[&<>'"]/g, 
    tag => ({
      '&': '&amp;',
      '<': '&lt;',
      '>': '&gt;',
      "'": '&#39;',
      '"': '&quot;'
    }[tag] || tag)
  );
}

// Helper functions for byte substring parsing
function substringByByte(str, maxLength) {
  var result = "";
  var flag = false;
  var len = 0;
  var length = 0;
  var length2 = 0;
  for (var i = 0; i < str.length; i++) {
    var code = str.codePointAt(i).toString(16);
    if (code.length > 4) {
      i++;
      if ((i + 1) < str.length) {
        flag = str.codePointAt(i + 1).toString(16) == "200d";
      }
    }
    if (flag) {
      len += getByteByHex(code);
      if (i == str.length - 1) {
        length += len;
        if (length <= maxLength) {
          result += str.substr(length2, i - length2 + 1);
        } else {
          break;
        }
      }
    } else {
      if (len != 0) {
        length += len;
        length += getByteByHex(code);
        if (length <= maxLength) {
          result += str.substr(length2, i - length2 + 1);
          length2 = i + 1;
        } else {
          break;
        }
        len = 0;
        continue;
      }
      length += getByteByHex(code);
      if (length <= maxLength) {
        if (code.length <= 4) {
          result += str[i];
        } else {
          result += str[i - 1] + str[i];
        }
        length2 = i + 1;
      } else {
        break;
      }
    }
  }
  return result;
}

function getByteByBinary(binaryCode) {
  var byteLengthDatas = [0, 1, 2, 3, 4];
  return byteLengthDatas[Math.ceil(binaryCode.length / 8)];
}

function getByteByHex(hexCode) {
  return getByteByBinary(parseInt(hexCode, 16).toString(2));
}
