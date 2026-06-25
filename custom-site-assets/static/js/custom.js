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

  // Persist sidebar scroll position across page reloads
  initSidebarScrollPreserve();

  // Initialize Table of Contents ScrollSpy
  initTocScrollSpy();

  // Fix and initialize collapsible sidebar folders
  initCollapsibleSidebar();
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

// Persist sidebar scroll position across page reloads
function initSidebarScrollPreserve() {
  const sidebar = document.querySelector('.docs-sidebar');
  if (sidebar) {
    // Restore scroll position
    const savedScrollTop = sessionStorage.getItem('sidebar-scroll');
    if (savedScrollTop) {
      sidebar.scrollTop = parseInt(savedScrollTop, 10);
    }

    // Save scroll position on scroll
    sidebar.addEventListener('scroll', () => {
      sessionStorage.setItem('sidebar-scroll', sidebar.scrollTop);
    }, { passive: true });
  }
}

// Table of Contents ScrollSpy using IntersectionObserver
function initTocScrollSpy() {
  const tocLinks = document.querySelectorAll('#TableOfContents a');
  const headings = Array.from(document.querySelectorAll('.docs-content h2, .docs-content h3'));

  if (tocLinks.length > 0 && headings.length > 0) {
    const activeClass = 'active';
    let activeHeading = null;

    const observerOptions = {
      root: null,
      rootMargin: '-10% 0px -75% 0px', // Trigger when heading is in upper section of viewport
      threshold: 0
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          activeHeading = entry.target;
          updateActiveTocLink();
        }
      });
    }, observerOptions);

    headings.forEach((heading) => observer.observe(heading));

    function updateActiveTocLink() {
      if (!activeHeading) return;
      const id = activeHeading.getAttribute('id');
      if (!id) return;

      tocLinks.forEach((link) => {
        const href = link.getAttribute('href');
        if (href && href.endsWith('#' + id)) {
          link.classList.add(activeClass);
          // Scroll the active link into view inside the TOC container if it overflows
          link.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        } else {
          link.classList.remove(activeClass);
        }
      });
    }

    // Fallback: if scrolled to the very top, highlight the first TOC link
    window.addEventListener('scroll', () => {
      if (window.scrollY < 100) {
        tocLinks.forEach((link, idx) => {
          if (idx === 0) link.classList.add(activeClass);
          else link.classList.remove(activeClass);
        });
      }
    }, { passive: true });
  }
}

// Fix collapsible sidebar categories (handles nested folders and folders without direct pages)
function initCollapsibleSidebar() {
  const sections = document.querySelectorAll('.collapsible-section');
  if (sections.length === 0) return;

  const isSidebarCollapsed = typeof sidebar_collapsed !== 'undefined' ? sidebar_collapsed : false;

  sections.forEach((section) => {
    const wrapper = section.nextElementSibling;
    if (!wrapper || !wrapper.classList.contains('collapsible-wrapper')) return;

    // Auto-expand folder if it contains the currently active note/link
    const hasActiveLink = wrapper.querySelector('a.active') !== null;
    
    if (hasActiveLink || !isSidebarCollapsed) {
      section.classList.add('open');
      wrapper.classList.add('open');
      wrapper.style.height = 'auto';
    } else {
      section.classList.remove('open');
      wrapper.classList.remove('open');
      wrapper.style.height = '0px';
    }

    // Clone to remove old click event listener from main.js
    const newSection = section.cloneNode(true);
    section.parentNode.replaceChild(newSection, section);

    newSection.addEventListener('click', (e) => {
      e.preventDefault();
      newSection.classList.toggle('open');
      wrapper.classList.toggle('open');
      
      if (wrapper.classList.contains('open')) {
        wrapper.style.height = 'auto';
      } else {
        wrapper.style.height = '0px';
      }
    });
  });
}
