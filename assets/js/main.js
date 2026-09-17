// Learn Japanese with Raj — shared site behaviour

// Captured now — document.currentScript is only reliable during this
// script's initial synchronous run, not later inside event handlers.
const CURRENT_SCRIPT_SRC = document.currentScript ? document.currentScript.src : null;

// ---------- theme (light/dark) ----------
// Applied immediately (script runs at the end of body, so the DOM already
// exists) to minimize the flash before DOMContentLoaded-driven UI wiring below.
const THEME_KEY = "ljwr-theme";

function getStoredTheme() {
  try {
    return localStorage.getItem(THEME_KEY);
  } catch (e) {
    return null;
  }
}

function getEffectiveTheme() {
  const stored = getStoredTheme();
  if (stored === "light" || stored === "dark") return stored;
  return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches
    ? "dark"
    : "light";
}

function applyTheme(theme) {
  document.documentElement.setAttribute("data-theme", theme);
}

// Apply any saved preference right away, before the rest of the page logic runs.
(() => {
  const stored = getStoredTheme();
  if (stored === "light" || stored === "dark") applyTheme(stored);
})();

document.addEventListener("DOMContentLoaded", () => {
  // Theme toggle button — injected into every page's header so no page
  // template needs to be edited by hand.
  document.querySelectorAll(".site-header .container").forEach((container) => {
    const navLinks = container.querySelector(".nav-links");
    const navToggleBtn = container.querySelector(".nav-toggle");
    if (!navLinks && !navToggleBtn) return;

    const controls = document.createElement("div");
    controls.className = "header-controls";
    const anchor = navLinks || navToggleBtn;
    container.insertBefore(controls, anchor);

    if (navLinks) controls.appendChild(navLinks);

    const themeBtn = document.createElement("button");
    themeBtn.type = "button";
    themeBtn.className = "theme-toggle";
    controls.appendChild(themeBtn);

    if (CURRENT_SCRIPT_SRC) {
      const logoutBtn = document.createElement("button");
      logoutBtn.type = "button";
      logoutBtn.className = "logout-btn";
      logoutBtn.textContent = "Log out";
      logoutBtn.addEventListener("click", () => {
        try {
          localStorage.removeItem("ljwr-auth");
        } catch (e) {
          /* ignore (private browsing, storage disabled, etc.) */
        }
        location.href = new URL("../../login.html", CURRENT_SCRIPT_SRC).href;
      });
      controls.appendChild(logoutBtn);
    }

    if (navToggleBtn) controls.appendChild(navToggleBtn);

    const render = () => {
      const theme = getEffectiveTheme();
      themeBtn.textContent = theme === "dark" ? "☀️" : "🌙";
      themeBtn.setAttribute(
        "aria-label",
        theme === "dark" ? "Switch to light mode" : "Switch to dark mode"
      );
    };
    render();

    themeBtn.addEventListener("click", () => {
      const next = getEffectiveTheme() === "dark" ? "light" : "dark";
      try {
        localStorage.setItem(THEME_KEY, next);
      } catch (e) {
        /* ignore (private browsing, storage disabled, etc.) */
      }
      applyTheme(next);
      render();
    });
  });

  // Mobile nav toggle
  const navToggle = document.querySelector(".nav-toggle");
  const navLinks = document.querySelector(".nav-links");
  if (navToggle && navLinks) {
    navToggle.addEventListener("click", () => {
      navLinks.classList.toggle("open");
    });
    navLinks.querySelectorAll("a").forEach((link) => {
      link.addEventListener("click", () => navLinks.classList.remove("open"));
    });
  }

  // Generic show/hide toggle: <button data-toggle="#targetId">
  document.querySelectorAll("[data-toggle]").forEach((btn) => {
    const target = document.querySelector(btn.getAttribute("data-toggle"));
    if (!target) return;
    btn.addEventListener("click", () => {
      target.classList.toggle("open");
      const showText = btn.getAttribute("data-toggle-show");
      const hideText = btn.getAttribute("data-toggle-hide");
      if (showText && hideText) {
        btn.textContent = target.classList.contains("open") ? hideText : showText;
      }
    });
  });

  // Card search filter: <input data-search-input> filters [data-search-target] items
  const searchInput = document.querySelector("[data-search-input]");
  if (searchInput) {
    const cards = document.querySelectorAll("[data-search-target]");
    searchInput.addEventListener("input", () => {
      const q = searchInput.value.trim().toLowerCase();
      cards.forEach((card) => {
        const haystack = card.getAttribute("data-search-target").toLowerCase();
        card.style.display = haystack.includes(q) ? "" : "none";
      });
    });
  }

  // Word glossary tooltip: <span class="wt" data-romaji="" data-en="" data-hi="" data-gu="">word</span>
  // Hover shows it (desktop); clicking/tapping pins it open until you click
  // elsewhere, click the word again, or press Escape — works without hover
  // on touch devices since tap fires a click event too.
  const wtTriggers = document.querySelectorAll(".wt");
  if (wtTriggers.length) {
    const popup = document.createElement("div");
    popup.className = "wt-popup";
    popup.setAttribute("role", "tooltip");
    document.body.appendChild(popup);

    let activeTrigger = null;

    const buildContent = (trigger) => {
      const romaji = trigger.getAttribute("data-romaji");
      const en = trigger.getAttribute("data-en");
      const hi = trigger.getAttribute("data-hi");
      const gu = trigger.getAttribute("data-gu");
      let html = "";
      if (romaji) html += `<div class="wt-romaji">${romaji}</div>`;
      if (en) html += `<div><b>EN</b> ${en}</div>`;
      if (hi) html += `<div><b>HI</b> ${hi}</div>`;
      if (gu) html += `<div><b>GU</b> ${gu}</div>`;
      return html;
    };

    const positionPopup = (trigger) => {
      const rect = trigger.getBoundingClientRect();
      const popupRect = popup.getBoundingClientRect();
      let left = rect.left + rect.width / 2 - popupRect.width / 2 + window.scrollX;
      const minLeft = window.scrollX + 8;
      const maxLeft = window.scrollX + document.documentElement.clientWidth - popupRect.width - 8;
      left = Math.max(minLeft, Math.min(left, maxLeft));
      let top = rect.top + window.scrollY - popupRect.height - 10;
      if (top < window.scrollY + 8) top = rect.bottom + window.scrollY + 10;
      popup.style.left = `${left}px`;
      popup.style.top = `${top}px`;
    };

    const showPopup = (trigger) => {
      activeTrigger = trigger;
      popup.innerHTML = buildContent(trigger);
      popup.classList.add("open");
      positionPopup(trigger);
    };

    const hidePopup = () => {
      activeTrigger = null;
      popup.classList.remove("open");
    };

    const unpinAll = () => wtTriggers.forEach((t) => t.classList.remove("wt-pinned"));

    wtTriggers.forEach((trigger) => {
      trigger.addEventListener("mouseenter", () => {
        if (!trigger.classList.contains("wt-pinned")) showPopup(trigger);
      });
      trigger.addEventListener("mouseleave", () => {
        if (!trigger.classList.contains("wt-pinned")) hidePopup();
      });
      trigger.addEventListener("click", (e) => {
        e.stopPropagation();
        const wasPinned = trigger.classList.contains("wt-pinned");
        unpinAll();
        if (wasPinned) {
          hidePopup();
        } else {
          trigger.classList.add("wt-pinned");
          showPopup(trigger);
        }
      });
    });

    document.addEventListener("click", () => {
      unpinAll();
      hidePopup();
    });

    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape") {
        unpinAll();
        hidePopup();
      }
    });

    window.addEventListener(
      "scroll",
      () => {
        if (activeTrigger) positionPopup(activeTrigger);
      },
      { passive: true }
    );
  }

  // Quiz answer reveal: click a .choice to mark correct/wrong
  document.querySelectorAll(".quiz-item").forEach((item) => {
    const choices = item.querySelectorAll(".choice");
    choices.forEach((choice) => {
      choice.addEventListener("click", () => {
        if (item.classList.contains("answered")) return;
        item.classList.add("answered");
        choices.forEach((c) => {
          if (c.getAttribute("data-correct") === "true") {
            c.classList.add("correct");
          } else if (c === choice) {
            c.classList.add("wrong");
          }
        });
      });
    });
  });
});
