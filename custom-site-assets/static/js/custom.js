/**
 * Custom micro-interactions and dynamic enhancement for Gianfranco's Second Brain
 */
document.addEventListener('DOMContentLoaded', () => {
  // Create mouse-glow element
  const glow = document.createElement('div');
  glow.id = 'glow-pointer';
  document.body.appendChild(glow);

  // Follow cursor
  document.addEventListener('mousemove', (e) => {
    glow.style.left = e.clientX + 'px';
    glow.style.top = e.clientY + 'px';
  });

  // Dynamically style inline hashtags
  formatHashtags();
});

// Helper to escape HTML characters
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

// Function to dynamically wrap hashtags in note content
function formatHashtags() {
  const content = document.querySelector('.docs-content');
  if (!content) return;

  const hashtagRegex = /(^|\s)(#[a-zA-Z0-9_\-\/]+)/g;

  // Helper to recursively traverse text nodes
  function traverse(node) {
    // Skip specific elements to avoid breaking them
    const skipTags = ['A', 'CODE', 'PRE', 'SCRIPT', 'STYLE', 'BUTTON', 'INPUT', 'TEXTAREA', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6'];
    if (node.nodeType === Node.ELEMENT_NODE) {
      if (skipTags.includes(node.tagName)) return;
    }

    if (node.nodeType === Node.TEXT_NODE) {
      const text = node.nodeValue;
      if (text.includes('#')) {
        // Reset regex index
        hashtagRegex.lastIndex = 0;
        if (hashtagRegex.test(text)) {
          hashtagRegex.lastIndex = 0;
          
          const tempSpan = document.createElement('span');
          const escapedText = escapeHTML(text);
          tempSpan.innerHTML = escapedText.replace(hashtagRegex, (match, space, hashtag) => {
            let categoryClass = '';
            const tagLower = hashtag.toLowerCase();
            if (tagLower.includes('paper')) categoryClass = ' tag-paper';
            else if (tagLower.includes('study') || tagLower.includes('guide')) categoryClass = ' tag-study';
            else if (tagLower.includes('security') || tagLower.includes('oscp') || tagLower.includes('cyber')) categoryClass = ' tag-security';
            else if (tagLower.includes('ml') || tagLower.includes('agentic')) categoryClass = ' tag-ml';
            else if (tagLower.includes('ops') || tagLower.includes('mcp')) categoryClass = ' tag-mlops';
            
            return `${space}<span class="tag${categoryClass}">${hashtag}</span>`;
          });
          
          const parent = node.parentNode;
          if (parent) {
            while (tempSpan.firstChild) {
              parent.insertBefore(tempSpan.firstChild, node);
            }
            parent.removeChild(node);
          }
        }
      }
      return;
    }

    // Traverse children
    const children = Array.from(node.childNodes);
    for (const child of children) {
      traverse(child);
    }
  }

  traverse(content);
}

