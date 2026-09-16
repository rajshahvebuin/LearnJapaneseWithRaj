// Learn Japanese with Raj — simple client-side access gate
//
// This only deters casual visitors; it is not real security. The page
// itself (and this script) are visible to anyone who opens dev tools, so
// never rely on this to protect anything sensitive.
(function () {
  var AUTH_KEY = "ljwr-auth";
  var currentScript = document.currentScript;

  function isAuthed() {
    try {
      return localStorage.getItem(AUTH_KEY) === "1";
    } catch (e) {
      return false;
    }
  }

  if (isAuthed()) return;

  var loginUrl = new URL("../../login.html", currentScript.src).href;
  var redirect = encodeURIComponent(
    location.pathname + location.search + location.hash
  );
  location.replace(loginUrl + "?redirect=" + redirect);

  // Stop the rest of the page from rendering while the redirect happens.
  document.documentElement.style.display = "none";
})();
