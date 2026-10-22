/* Gute Nacht, Spielzeug – site script (no tracking, no external requests) */

/* ===== App Store switch: set to true once the app is live ===== */
var APP_STORE_LIVE = false;
var APP_STORE_URL = "https://apps.apple.com/app/id6824285939";

(function () {
  var en = document.documentElement.lang === "en";

  // App Store call-to-action buttons
  document.querySelectorAll("[data-appstore]").forEach(function (el) {
    if (APP_STORE_LIVE) {
      var a = document.createElement("a");
      a.className = el.className.replace("is-soon", "");
      a.href = APP_STORE_URL;
      a.rel = "noopener";
      a.innerHTML = '<span class="as-small">' + (en ? "Download on the" : "Laden im") + '</span><span class="as-big">App Store</span>';
      el.replaceWith(a);
    }
  });

  // Obfuscated support e-mail
  var u = "mip", d = "gmx" + "." + "biz";
  document.querySelectorAll("[data-mail]").forEach(function (el) {
    var addr = u + "@" + d;
    var a = document.createElement("a");
    a.href = "mai" + "lto:" + addr + (el.dataset.mail ? "?subject=" + encodeURIComponent(el.dataset.mail) : "");
    a.textContent = addr;
    el.textContent = "";
    el.appendChild(a);
  });
})();
