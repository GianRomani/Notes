/**
 * Custom micro-interactions and dynamic enhancement for Gianfranco's Second Brain
 */
document.addEventListener("DOMContentLoaded", () => {
  // Create mouse-glow element
  const glow = document.createElement("div");
  glow.id = "glow-pointer";
  document.body.appendChild(glow);

  // Follow cursor
  document.addEventListener("mousemove", (e) => {
    glow.style.left = e.clientX + "px";
    glow.style.top = e.clientY + "px";
  });

  // Dynamically style inline hashtags
  formatHashtags();

  // Persist sidebar scroll position across page reloads
  initSidebarScrollPreserve();

  // Initialize Table of Contents ScrollSpy
  initTocScrollSpy();

  // Fix and initialize collapsible sidebar folders
  initCollapsibleSidebar();

  // Initialize mobile off-canvas drawer navigation
  initMobileDrawer();
});

// Helper to escape HTML characters
function escapeHTML(str) {
  return str.replace(
    /[&<>'"]/g,
    (tag) =>
      ({
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        "'": "&#39;",
        '"': "&quot;",
      })[tag] || tag,
  );
}

// Function to dynamically wrap hashtags in note content
function formatHashtags() {
  const content = document.querySelector(".docs-content");
  if (!content) return;

  const hashtagRegex = /(^|\s)(#[a-zA-Z0-9_\-\/]+)/g;

  // Helper to recursively traverse text nodes
  function traverse(node) {
    // Skip specific elements to avoid breaking them
    const skipTags = [
      "A",
      "CODE",
      "PRE",
      "SCRIPT",
      "STYLE",
      "BUTTON",
      "INPUT",
      "TEXTAREA",
      "H1",
      "H2",
      "H3",
      "H4",
      "H5",
      "H6",
    ];
    if (node.nodeType === Node.ELEMENT_NODE) {
      if (skipTags.includes(node.tagName)) return;
    }

    if (node.nodeType === Node.TEXT_NODE) {
      const text = node.nodeValue;
      if (text.includes("#")) {
        // Reset regex index
        hashtagRegex.lastIndex = 0;
        if (hashtagRegex.test(text)) {
          hashtagRegex.lastIndex = 0;

          const tempSpan = document.createElement("span");
          const escapedText = escapeHTML(text);
          tempSpan.innerHTML = escapedText.replace(
            hashtagRegex,
            (match, space, hashtag) => {
              let categoryClass = "";
              const tagLower = hashtag.toLowerCase();
              if (tagLower.includes("paper")) categoryClass = " tag-paper";
              else if (tagLower.includes("study") || tagLower.includes("guide"))
                categoryClass = " tag-study";
              else if (
                tagLower.includes("security") ||
                tagLower.includes("oscp") ||
                tagLower.includes("cyber")
              )
                categoryClass = " tag-security";
              else if (tagLower.includes("ml") || tagLower.includes("agentic"))
                categoryClass = " tag-ml";
              else if (tagLower.includes("ops") || tagLower.includes("mcp"))
                categoryClass = " tag-mlops";
              else if (tagLower.includes("coffee"))
                categoryClass = " tag-coffee";

              return `${space}<span class="tag${categoryClass}">${hashtag}</span>`;
            },
          );

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
  const sidebar = document.querySelector(".docs-sidebar");
  if (sidebar) {
    // Restore scroll position
    const savedScrollTop = sessionStorage.getItem("sidebar-scroll");
    if (savedScrollTop) {
      sidebar.scrollTop = parseInt(savedScrollTop, 10);
    }

    // Save scroll position on scroll
    sidebar.addEventListener(
      "scroll",
      () => {
        sessionStorage.setItem("sidebar-scroll", sidebar.scrollTop);
      },
      { passive: true },
    );
  }
}

// Table of Contents ScrollSpy using IntersectionObserver
function initTocScrollSpy() {
  const tocLinks = document.querySelectorAll("#TableOfContents a");
  const headings = Array.from(
    document.querySelectorAll(".docs-content h2, .docs-content h3"),
  );

  if (tocLinks.length > 0 && headings.length > 0) {
    const activeClass = "active";
    let activeHeading = null;

    const observerOptions = {
      root: null,
      rootMargin: "-10% 0px -75% 0px", // Trigger when heading is in upper section of viewport
      threshold: 0,
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
      const id = activeHeading.getAttribute("id");
      if (!id) return;

      const container = document.querySelector(".docs-toc");
      let activeLink = null;

      tocLinks.forEach((link) => {
        const href = link.getAttribute("href");
        if (href && href.endsWith("#" + id)) {
          link.classList.add(activeClass);
          activeLink = link;
        } else {
          link.classList.remove(activeClass);
        }
      });

      if (container && activeLink) {
        const containerRect = container.getBoundingClientRect();
        const linkRect = activeLink.getBoundingClientRect();

        // Calculate the relative top of the link inside the container
        const relativeTop =
          linkRect.top - containerRect.top + container.scrollTop;
        const linkHeight = linkRect.height;
        const containerHeight = containerRect.height;

        // Target scroll to center the active link in the viewport
        let targetScrollTop =
          relativeTop - containerHeight / 2 + linkHeight / 2;

        // Clamp scroll boundaries
        const maxScrollTop = container.scrollHeight - containerHeight;
        if (targetScrollTop < 0) {
          targetScrollTop = 0;
        } else if (targetScrollTop > maxScrollTop) {
          targetScrollTop = maxScrollTop;
        }

        container.scrollTo({
          top: targetScrollTop,
          behavior: "smooth",
        });
      }
    }

    // Scroll listener for Top and Bottom page fallbacks
    window.addEventListener(
      "scroll",
      () => {
        const scrollY = window.scrollY || document.documentElement.scrollTop;
        const windowHeight = window.innerHeight;
        const docHeight = document.documentElement.scrollHeight;
        const container = document.querySelector(".docs-toc");

        // Top fallback: highlight first TOC link and scroll TOC container to 0
        if (scrollY < 50) {
          tocLinks.forEach((link, idx) => {
            if (idx === 0) {
              link.classList.add(activeClass);
              if (container && container.scrollTop > 0) {
                container.scrollTo({ top: 0, behavior: "smooth" });
              }
            } else {
              link.classList.remove(activeClass);
            }
          });
          return;
        }

        // Bottom fallback: highlight last TOC link and scroll TOC container to bottom
        if (scrollY + windowHeight >= docHeight - 50) {
          tocLinks.forEach((link, idx) => {
            if (idx === tocLinks.length - 1) {
              link.classList.add(activeClass);
              if (container) {
                const maxScroll =
                  container.scrollHeight - container.clientHeight;
                if (container.scrollTop < maxScroll - 5) {
                  container.scrollTo({
                    top: container.scrollHeight,
                    behavior: "smooth",
                  });
                }
              }
            } else {
              link.classList.remove(activeClass);
            }
          });
          return;
        }
      },
      { passive: true },
    );
  }
}

// Fix collapsible sidebar categories (handles nested folders and folders without direct pages)
function initCollapsibleSidebar() {
  const sections = document.querySelectorAll(".collapsible-section");
  if (sections.length === 0) return;

  const isSidebarCollapsed =
    typeof sidebar_collapsed !== "undefined" ? sidebar_collapsed : false;

  sections.forEach((section) => {
    const wrapper = section.nextElementSibling;
    if (!wrapper || !wrapper.classList.contains("collapsible-wrapper")) return;

    // Auto-expand folder if it contains the currently active note/link
    const hasActiveLink = wrapper.querySelector("a.active") !== null;

    if (hasActiveLink || !isSidebarCollapsed) {
      section.classList.add("open");
      wrapper.classList.add("open");
      wrapper.style.height = "auto";
    } else {
      section.classList.remove("open");
      wrapper.classList.remove("open");
      wrapper.style.height = "0px";
    }

    // Clone to remove old click event listener from main.js
    const newSection = section.cloneNode(true);
    section.parentNode.replaceChild(newSection, section);

    newSection.addEventListener("click", (e) => {
      e.preventDefault();
      newSection.classList.toggle("open");
      wrapper.classList.toggle("open");

      if (wrapper.classList.contains("open")) {
        wrapper.style.height = "auto";
      } else {
        wrapper.style.height = "0px";
      }
    });
  });
}

// Initialize Mobile Navigation Off-Canvas Drawer
function initMobileDrawer() {
  const sidebar =
    document.getElementById("docs-sidebar") ||
    document.querySelector(".docs-sidebar");
  const backdrop = document.getElementById("sidebar-backdrop");
  const toggleBtn = document.getElementById("mobile-sidebar-toggle");
  const closeBtn = document.getElementById("sidebar-close-btn");
  const menuCheckbox = document.getElementById("menu-btn");

  if (!sidebar) return;

  function openDrawer() {
    sidebar.classList.add("drawer-open");
    if (backdrop) backdrop.classList.add("active");
    if (toggleBtn) {
      toggleBtn.setAttribute("aria-expanded", "true");
      toggleBtn.classList.add("active");
    }
    document.body.classList.add("drawer-locked");
  }

  function closeDrawer() {
    sidebar.classList.remove("drawer-open");
    if (backdrop) backdrop.classList.remove("active");
    if (toggleBtn) {
      toggleBtn.setAttribute("aria-expanded", "false");
      toggleBtn.classList.remove("active");
    }
    document.body.classList.remove("drawer-locked");
    if (menuCheckbox) menuCheckbox.checked = false;
  }

  if (toggleBtn) {
    toggleBtn.addEventListener("click", (e) => {
      e.preventDefault();
      e.stopPropagation();
      if (sidebar.classList.contains("drawer-open")) {
        closeDrawer();
      } else {
        openDrawer();
      }
    });
  }

  // Support clicking fallback menu icon if present
  const menuIcon = document.querySelector(".menu-icon");
  if (menuIcon) {
    menuIcon.addEventListener("click", (e) => {
      e.preventDefault();
      e.stopPropagation();
      if (sidebar.classList.contains("drawer-open")) {
        closeDrawer();
      } else {
        openDrawer();
      }
    });
  }

  if (closeBtn) {
    closeBtn.addEventListener("click", (e) => {
      e.preventDefault();
      closeDrawer();
    });
  }

  if (backdrop) {
    backdrop.addEventListener("click", (e) => {
      e.preventDefault();
      closeDrawer();
    });
  }

  // Close drawer when a note link is clicked on mobile
  const sidebarLinks = sidebar.querySelectorAll("a.docs-link");
  sidebarLinks.forEach((link) => {
    link.addEventListener("click", () => {
      if (window.innerWidth < 992) {
        closeDrawer();
      }
    });
  });

  // ESC key closes drawer
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && sidebar.classList.contains("drawer-open")) {
      closeDrawer();
    }
  });

  // Close drawer if viewport resizes above desktop threshold
  window.addEventListener(
    "resize",
    () => {
      if (
        window.innerWidth >= 992 &&
        sidebar.classList.contains("drawer-open")
      ) {
        closeDrawer();
      }
    },
    { passive: true },
  );
}
