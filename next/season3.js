/* Season 3 · live countdowns on fixture tickets.
   Markup carries the full kickoff text, so with script off every ticket still
   reads correctly. Script only adds the countdown line and marks the next match. */
(function () {
  "use strict";
  /* the big countdown on the front page; markup already states the kickoff in words */
  var cd = document.querySelector("[data-countdown]");
  if (cd) {
    var k0 = Date.parse(cd.getAttribute("data-countdown"));
    var cell = function (u) { return cd.querySelector('[data-u="' + u + '"]'); };
    var pad = function (n) { return (n < 10 ? "0" : "") + n; };
    var paint = function () {
      var ms = k0 - Date.now();
      if (isNaN(k0) || ms <= 0) { cd.classList.add("is-static"); return; }
      cd.classList.remove("is-static"); var s = Math.floor(ms / 1000);
      cell("d").textContent = Math.floor(s / 86400); cell("h").textContent = pad(Math.floor(s % 86400 / 3600));
      cell("m").textContent = pad(Math.floor(s % 3600 / 60)); cell("s").textContent = pad(s % 60);
    };
    paint(); setInterval(paint, 1000);
  }
  var tickets = Array.prototype.slice.call(document.querySelectorAll("[data-kick]"));
  if (!tickets.length) return;
  function fmt(ms) {
    var m = Math.floor(ms / 60000), d = Math.floor(m / 1440), h = Math.floor((m % 1440) / 60), mm = m % 60;
    if (d > 0) return d + (d === 1 ? " day " : " days ") + h + " hr";
    if (h > 0) return h + " hr " + mm + " min";
    return mm + " min";
  }
  function tick() {
    var now = Date.now(), nextSet = false;
    tickets.forEach(function (el) {
      var k = Date.parse(el.getAttribute("data-kick"));
      var out = el.querySelector(".fixture__cd");
      el.classList.remove("is-next");
      if (!out || isNaN(k)) return;
      if (now < k) {
        out.textContent = "Kickoff in " + fmt(k - now);
        if (!nextSet) { el.classList.add("is-next"); nextSet = true; }
      } else if (now < k + 2 * 3600 * 1000) {
        out.textContent = "Live now, probably. Go.";
        el.classList.add("is-next"); nextSet = true;
      } else {
        out.textContent = "Played. Result goes on this page once it is receipted.";
      }
    });
  }
  tick();
  setInterval(tick, 30000);
})();
