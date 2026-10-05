// Library page: search + level/status filters (progressive enhancement —
// every book is in the HTML, this only hides what doesn't match).
(function () {
  var search = document.querySelector("[data-lib-search]");
  if (!search) return;
  var cards = Array.prototype.slice.call(document.querySelectorAll(".book-card[data-search]"));
  var levelChips = document.querySelectorAll("[data-filter-level]");
  var statusChip = document.querySelector("[data-filter-status]");
  var empty = document.querySelector("[data-lib-empty]");
  var level = null, readyOnly = false;

  function apply() {
    var q = search.value.trim().toLowerCase();
    var shown = 0;
    cards.forEach(function (c) {
      var ok = (!q || c.getAttribute("data-search").indexOf(q) !== -1) &&
               (!level || c.getAttribute("data-level") === level) &&
               (!readyOnly || c.getAttribute("data-status") === "ready");
      c.style.display = ok ? "" : "none";
      if (ok) shown++;
    });
    document.querySelectorAll(".lib-module").forEach(function (m) {
      var any = m.querySelector('.book-card:not([style*="none"])');
      m.style.display = any ? "" : "none";
    });
    document.querySelectorAll("[data-level-section]").forEach(function (s) {
      var any = s.querySelector('.lib-module:not([style*="none"])');
      s.style.display = any ? "" : "none";
    });
    if (empty) empty.style.display = shown ? "none" : "block";
  }

  search.addEventListener("input", apply);
  levelChips.forEach(function (chip) {
    chip.addEventListener("click", function () {
      var v = chip.getAttribute("data-filter-level");
      level = level === v ? null : v;
      levelChips.forEach(function (c) { c.setAttribute("aria-pressed", String(c.getAttribute("data-filter-level") === level)); });
      apply();
    });
  });
  if (statusChip) statusChip.addEventListener("click", function () {
    readyOnly = !readyOnly;
    statusChip.setAttribute("aria-pressed", String(readyOnly));
    apply();
  });
  var lv = new URLSearchParams(location.search).get("level");
  if (lv) { var c = document.querySelector('[data-filter-level="' + lv + '"]'); if (c) c.click(); }
})();
