// Learn Japanese with Raj — login page logic
(function () {
  var AUTH_KEY = "ljwr-auth";
  var USERNAME = "Learn";
  var PASSWORD = "Japanese";

  function getRedirectTarget() {
    var params = new URLSearchParams(location.search);
    var redirect = params.get("redirect");
    if (!redirect) return "index.html";
    // Only ever follow a same-site path, never an absolute/external URL.
    if (!redirect.startsWith("/") || redirect.startsWith("//")) {
      return "index.html";
    }
    return redirect;
  }

  function isAuthed() {
    try {
      return localStorage.getItem(AUTH_KEY) === "1";
    } catch (e) {
      return false;
    }
  }

  if (isAuthed()) {
    location.replace(getRedirectTarget());
    return;
  }

  document.addEventListener("DOMContentLoaded", function () {
    var form = document.getElementById("login-form");
    var errorEl = document.getElementById("login-error");
    if (!form) return;

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var username = form.username.value.trim();
      var password = form.password.value;

      if (username === USERNAME && password === PASSWORD) {
        try {
          localStorage.setItem(AUTH_KEY, "1");
        } catch (err) {
          /* ignore (private browsing, storage disabled, etc.) */
        }
        location.replace(getRedirectTarget());
      } else {
        if (errorEl) errorEl.textContent = "Incorrect username or password.";
        form.password.value = "";
        form.password.focus();
      }
    });
  });
})();
