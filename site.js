(function () {
  "use strict";
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches || !("IntersectionObserver" in window)) return;
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
    });
  }, { rootMargin: "0px 0px -8% 0px" });
  document.querySelectorAll(".friend-card, .ledger, .profile-card, .kit-card, .lore-entry, details, .cta").forEach(function (el) {
    el.classList.add("reveal");
    io.observe(el);
  });
})();
