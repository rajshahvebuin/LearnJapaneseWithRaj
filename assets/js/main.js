// Learn Japanese with Raj — shared site behaviour

document.addEventListener("DOMContentLoaded", () => {
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
