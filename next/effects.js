/* effects.js · v3 cohesion kit · shared behavior for every page. No dependencies. */
(function () {
  "use strict";

  var PAGES = [
    ["index", "Home"], ["journey", "Journey"], ["run", "Run"], ["groupd", "Grp D"],
    ["r32", "R32"], ["r16", "R16"], ["friends", "Friends"], ["roster", "Roster"],
    ["strategy", "Strat"], ["kits", "Kits"], ["lore", "Lore"], ["guide", "Guide"],
    ["meta", "Making"]
  ];
  var LS_KEY = "usmnt_v1";
  var rm = function () { return window.matchMedia("(prefers-reduced-motion: reduce)").matches; };

  /* ---------- store ---------- */
  var store = {
    read: function () { try { return JSON.parse(localStorage.getItem(LS_KEY) || "{}"); } catch (e) { return {}; } },
    write: function (s) { try { localStorage.setItem(LS_KEY, JSON.stringify(s)); } catch (e) { } },
    get: function (k) { return store.read()[k]; },
    set: function (k, v) { var s = store.read(); s[k] = v; store.write(s); }
  };

  /* ---------- sound ---------- */
  var audioCtx = null;
  function ctx() {
    if (!audioCtx) {
      var AC = window.AudioContext || window.webkitAudioContext;
      if (AC) audioCtx = new AC();
    }
    return audioCtx;
  }
  var sound = {
    on: function () { return !!store.get("sound"); },
    toggle: function () {
      var v = !sound.on();
      store.set("sound", v);
      var btn = document.getElementById("sound-toggle");
      if (btn) { btn.setAttribute("aria-pressed", String(v)); btn.textContent = v ? "♪ on" : "♪ off"; }
      if (v) { ctx(); sound.chime(true); }
    },
    chime: function (up) {
      if (!sound.on() || rm()) return;
      var c = ctx(); if (!c) return;
      var t = c.currentTime;
      var freqs = up ? [523, 784] : [392, 330];
      freqs.forEach(function (f, i) {
        var o = c.createOscillator(), g = c.createGain();
        o.frequency.value = f; o.type = "sine";
        g.gain.setValueAtTime(0.001, t + i * 0.09);
        g.gain.exponentialRampToValueAtTime(0.05, t + i * 0.09 + 0.02);
        g.gain.exponentialRampToValueAtTime(0.001, t + i * 0.09 + 0.3);
        o.connect(g); g.connect(c.destination);
        o.start(t + i * 0.09); o.stop(t + i * 0.09 + 0.32);
      });
    }
  };

  /* ---------- reveal ---------- */
  var io = null;
  function reveal(root) {
    root = root || document;
    if (!("IntersectionObserver" in window)) {
      root.querySelectorAll("[data-reveal],[data-reveal-group]").forEach(function (el) { el.classList.add("in"); });
      return;
    }
    if (!io) {
      io = new IntersectionObserver(function (es) {
        es.forEach(function (e) {
          if (!e.isIntersecting) return;
          e.target.classList.add("in");
          e.target.querySelectorAll(".stat__num[data-count]").forEach(countUp);
          io.unobserve(e.target);
        });
      }, { rootMargin: "0px 0px -10% 0px" });
    }
    root.querySelectorAll("[data-reveal],[data-reveal-group]").forEach(function (el) { io.observe(el); });
    root.querySelectorAll("[data-reveal-group]").forEach(function (g) {
      Array.prototype.forEach.call(g.children, function (c, i) { c.style.setProperty("--i", i); });
    });
    root.querySelectorAll(".kinetic").forEach(function (h) {
      Array.prototype.forEach.call(h.querySelectorAll("span"), function (s, i) { s.style.setProperty("--i", i); });
    });
  }

  /* ---------- count-up ---------- */
  function countUp(el) {
    if (el.dataset.done) return;
    el.dataset.done = "1";
    var end = parseFloat(el.dataset.count || "0");
    var fmt = function (n) { return Math.round(n).toLocaleString("en-US"); };
    if (rm()) { el.textContent = fmt(end); return; }
    var dur = 900, t0 = performance.now();
    (function frame(t) {
      var p = Math.min((t - t0) / dur, 1), e = 1 - Math.pow(1 - p, 3);
      el.textContent = fmt(end * e);
      if (p < 1) requestAnimationFrame(frame);
    })(t0);
  }

  /* ---------- lightbox ---------- */
  var lb = { dlg: null, items: [], idx: 0 };
  function lbBuild() {
    if (lb.dlg) return;
    var d = document.createElement("dialog");
    d.className = "lb";
    d.innerHTML = '<figure><img alt=""/><figcaption></figcaption></figure>' +
      '<div class="lb__nav"><button data-nav="-1" aria-label="Previous">←</button>' +
      '<button data-nav="close" aria-label="Close">✕</button>' +
      '<button data-nav="1" aria-label="Next">→</button></div>';
    document.body.appendChild(d);
    d.addEventListener("click", function (ev) {
      var b = ev.target.closest("button");
      if (b) { b.dataset.nav === "close" ? d.close() : lbNav(parseInt(b.dataset.nav, 10)); return; }
      if (ev.target === d) d.close();
    });
    d.addEventListener("keydown", function (ev) {
      if (ev.key === "ArrowRight") lbNav(1);
      if (ev.key === "ArrowLeft") lbNav(-1);
    });
    var x0 = 0;
    d.addEventListener("touchstart", function (ev) { x0 = ev.touches[0].clientX; }, { passive: true });
    d.addEventListener("touchend", function (ev) {
      var dx = ev.changedTouches[0].clientX - x0;
      if (Math.abs(dx) > 48) lbNav(dx < 0 ? 1 : -1);
    }, { passive: true });
    lb.dlg = d;
  }
  function lbShow() {
    var it = lb.items[lb.idx];
    if (!it) return;
    var img = lb.dlg.querySelector("img"), cap = lb.dlg.querySelector("figcaption");
    img.src = it.href; img.alt = it.alt || "";
    cap.textContent = it.caption || "";
  }
  function lbNav(d) { lb.idx = (lb.idx + d + lb.items.length) % lb.items.length; lbShow(); }
  function lbOpen(items, idx) {
    lbBuild();
    lb.items = items; lb.idx = idx || 0;
    lbShow();
    if (!lb.dlg.open) lb.dlg.showModal();
  }
  function wireLightbox() {
    var links = Array.prototype.slice.call(document.querySelectorAll("a[data-lightbox]"));
    if (!links.length) return;
    var items = links.map(function (a) {
      var im = a.querySelector("img");
      return { href: a.getAttribute("href"), caption: a.dataset.caption || "", alt: im ? im.alt : "" };
    });
    links.forEach(function (a, i) {
      a.addEventListener("click", function (ev) { ev.preventDefault(); lbOpen(items, i); });
    });
  }

  /* ---------- confetti ---------- */
  function confetti(x, y) {
    if (rm()) return;
    x = x == null ? 0.5 : x; y = y == null ? 0.4 : y;
    var c = document.createElement("canvas");
    c.className = "fx-confetti";
    c.width = window.innerWidth; c.height = window.innerHeight;
    document.body.appendChild(c);
    var g = c.getContext("2d");
    var colors = ["#BF0A30", "#F5F1E8", "#3C3B6E", "#FFCD00"];
    var ps = [];
    for (var i = 0; i < 130; i++) {
      ps.push({
        x: c.width * x, y: c.height * y,
        vx: (Math.random() - 0.5) * 10, vy: -Math.random() * 11 - 3,
        r: 3 + Math.random() * 4, rot: Math.random() * 6.3, vr: (Math.random() - 0.5) * 0.3,
        color: colors[Math.random() * 4 | 0]
      });
    }
    (function frame() {
      g.clearRect(0, 0, c.width, c.height);
      var live = 0;
      ps.forEach(function (p) {
        p.vy += 0.3; p.x += p.vx; p.y += p.vy; p.rot += p.vr;
        if (p.y < c.height + 20) live++;
        g.save(); g.translate(p.x, p.y); g.rotate(p.rot);
        g.fillStyle = p.color; g.fillRect(-p.r, -p.r / 2, p.r * 2, p.r);
        g.restore();
      });
      live ? requestAnimationFrame(frame) : c.remove();
    })();
  }

  /* ---------- hold to reveal ---------- */
  function holdToReveal(btn) {
    var target = document.querySelector(btn.dataset.target);
    var ring = btn.querySelector(".hold__ring");
    if (!target) return;
    var CIRC = 2 * Math.PI * 11;
    if (ring) { ring.style.strokeDasharray = CIRC; ring.style.strokeDashoffset = CIRC; }
    var t0 = 0, raf = 0;
    function open() {
      target.hidden = false;
      target.setAttribute("data-reveal", "");
      reveal(target.parentNode);
      requestAnimationFrame(function () { target.classList.add("in"); });
      btn.style.display = "none";
      sound.chime(true);
    }
    function tick(t) {
      var p = Math.min((t - t0) / 900, 1);
      if (ring) ring.style.strokeDashoffset = CIRC * (1 - p);
      if (p < 1) raf = requestAnimationFrame(tick); else open();
    }
    function cancel() {
      cancelAnimationFrame(raf);
      if (ring) ring.style.strokeDashoffset = CIRC;
    }
    if (rm()) {
      btn.addEventListener("click", open);
    } else {
      btn.addEventListener("pointerdown", function (ev) { ev.preventDefault(); t0 = performance.now(); raf = requestAnimationFrame(tick); });
      ["pointerup", "pointerleave", "pointercancel"].forEach(function (e) { btn.addEventListener(e, cancel); });
      btn.addEventListener("keydown", function (ev) { if (ev.key === "Enter" || ev.key === " ") { ev.preventDefault(); open(); } });
    }
  }

  /* ---------- predict ---------- */
  function predict(root) {
    var opts = root.querySelectorAll(".predict__opts button");
    var rev = root.querySelector(".predict__reveal");
    if (!rev) return;
    opts.forEach(function (b) {
      b.addEventListener("click", function () {
        if (root.dataset.answered) return;
        root.dataset.answered = "1";
        b.classList.add("picked");
        opts.forEach(function (o) { o.disabled = true; });
        rev.hidden = false;
        rev.setAttribute("data-reveal", "");
        reveal(root);
        requestAnimationFrame(function () { rev.classList.add("in"); });
        var correct = root.dataset.answer && b.dataset.v === root.dataset.answer;
        sound.chime(!!correct);
      });
    });
  }

  /* ---------- waveform audio player ---------- */
  function wavePlayer(root) {
    var audio = root.querySelector("audio");
    var wave = root.querySelector(".wave");
    var btn = root.querySelector(".wave-player__btn");
    var time = root.querySelector(".wave-player__time");
    if (!audio || !wave || !btn) return;
    var bars = [];
    for (var i = 0; i < 48; i++) {
      var b = document.createElement("i");
      b.style.setProperty("--h", (0.3 + 0.7 * Math.abs(Math.sin(i * 1.7 + 0.6))).toFixed(2));
      wave.appendChild(b); bars.push(b);
    }
    function fmtT(s) { s = Math.floor(s || 0); return Math.floor(s / 60) + ":" + ("0" + s % 60).slice(-2); }
    btn.addEventListener("click", function () {
      if (audio.paused) { audio.play(); btn.textContent = "❚❚"; }
      else { audio.pause(); btn.textContent = "▶"; }
    });
    audio.addEventListener("timeupdate", function () {
      var p = audio.duration ? audio.currentTime / audio.duration : 0;
      bars.forEach(function (b, i) { b.classList.toggle("lit", i <= p * 48); });
      if (time) time.textContent = fmtT(audio.currentTime);
    });
    audio.addEventListener("ended", function () { btn.textContent = "▶"; bars.forEach(function (b) { b.classList.remove("lit"); }); });
    wave.addEventListener("click", function (ev) {
      if (!audio.duration) return;
      var r = wave.getBoundingClientRect();
      audio.currentTime = audio.duration * ((ev.clientX - r.left) / r.width);
      if (audio.paused) { audio.play(); btn.textContent = "❚❚"; }
    });
  }

  /* ---------- scrolly ---------- */
  function scrolly(root) {
    var scene = root.querySelector(".scrolly__scene");
    var steps = root.querySelectorAll(".scrolly__step");
    if (!scene || !steps.length || !("IntersectionObserver" in window)) return;
    var sio = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting) scene.dataset.step = e.target.dataset.step || "0";
      });
    }, { threshold: 0.6 });
    steps.forEach(function (s) { sio.observe(s); });
  }

  /* ---------- passport ---------- */
  function passport() {
    var page = document.body.dataset.page;
    if (page) {
      var s = store.read();
      s.stamps = s.stamps || {};
      if (!s.stamps[page]) s.stamps[page] = Date.now();
      store.write(s);
    }
    var strip = document.querySelector(".passport");
    var st = store.read().stamps || {};
    if (strip) {
      strip.innerHTML = "";
      PAGES.forEach(function (p) {
        var li = document.createElement("li");
        li.className = "stamp" + (st[p[0]] ? " got" : "");
        li.dataset.page = p[0];
        li.textContent = p[1];
        strip.appendChild(li);
      });
      var note = document.createElement("li");
      note.className = "passport__note";
      var n = Object.keys(st).filter(function (k) { return PAGES.some(function (p) { return p[0] === k; }); }).length;
      note.textContent = n >= PAGES.length ? "Every chapter opened. That's the whole summer. 🇺🇸" : "Chapters opened: " + n + " of " + PAGES.length + ". The passport fills as you explore.";
      strip.appendChild(note);
    }
    var s2 = store.read();
    var opened = Object.keys(s2.stamps || {}).filter(function (k) { return PAGES.some(function (p) { return p[0] === k; }); }).length;
    if (opened >= PAGES.length && !s2.stampsDone) {
      s2.stampsDone = 1; store.write(s2);
      setTimeout(function () { confetti(0.5, 0.3); }, 600);
    }
    var greet = document.getElementById("greet");
    if (greet && document.body.dataset.page === "index") {
      var visits = (s2.visits || 0) + 1;
      s2.visits = visits; store.write(s2);
      if (visits > 1 && opened > 1 && opened < PAGES.length) {
        greet.textContent = "Welcome back. You have opened " + opened + " of " + PAGES.length + " chapters.";
      }
    }
  }

  /* ---------- sound toggle wiring ---------- */
  function wireSound() {
    var btn = document.getElementById("sound-toggle");
    if (!btn) return;
    btn.setAttribute("aria-pressed", String(sound.on()));
    btn.textContent = sound.on() ? "♪ on" : "♪ off";
    btn.addEventListener("click", sound.toggle);
  }

  /* ---------- global ---------- */
  document.addEventListener("visibilitychange", function () {
    if (document.hidden) document.querySelectorAll("audio,video").forEach(function (m) { if (!m.muted) m.pause(); });
  });

  window.FX = {
    reveal: reveal, countUp: countUp, confetti: confetti,
    lightbox: { open: lbOpen }, sound: sound, store: { get: store.get, set: store.set },
    holdToReveal: holdToReveal, predict: predict, wavePlayer: wavePlayer, scrolly: scrolly
  };

  document.addEventListener("DOMContentLoaded", function () {
    reveal(document);
    wireLightbox();
    wireSound();
    passport();
    document.querySelectorAll(".hold[data-target]").forEach(holdToReveal);
    document.querySelectorAll(".predict").forEach(predict);
    document.querySelectorAll(".wave-player").forEach(wavePlayer);
    document.querySelectorAll(".scrolly").forEach(scrolly);
    document.querySelectorAll(".flip").forEach(function (f) {
      f.setAttribute("aria-pressed", "false");
      f.addEventListener("click", function () {
        var on = f.classList.toggle("is-flipped");
        f.setAttribute("aria-pressed", String(on));
        sound.chime(false);
      });
    });
    document.querySelectorAll(".compare").forEach(function (c) {
      var r = c.querySelector(".compare__range");
      if (r) r.addEventListener("input", function () { c.style.setProperty("--pos", r.value + "%"); });
    });
  });
})();
