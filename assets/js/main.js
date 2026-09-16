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
      controls.insertBefore(logoutBtn, navToggleBtn || null);
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
