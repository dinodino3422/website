/* GM Marine Automation — progressive enhancement only.
   Every page works with JavaScript disabled: the nav is a plain list, the FAQ
   uses <details>, the form is a normal POST, and the entrance animations never
   arm because the `js` class on <html> is what puts elements in their hidden
   start state. Nothing here is load-bearing.

   Everything motion-related also checks prefers-reduced-motion and falls back
   to the static behaviour. */
(function () {
  "use strict";

  var root = document.documentElement;
  var EL = root.lang.indexOf("en") !== 0;
  var reduced = window.matchMedia
    ? window.matchMedia("(prefers-reduced-motion: reduce)").matches
    : false;
  var EASE = "cubic-bezier(.22,.61,.36,1)";

  /* Mobile navigation ------------------------------------------------------ */
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("primary-nav");

  if (toggle && nav) {
    var setOpen = function (open) {
      toggle.setAttribute("aria-expanded", String(open));
      nav.setAttribute("data-open", String(open));
    };

    toggle.addEventListener("click", function () {
      setOpen(toggle.getAttribute("aria-expanded") !== "true");
    });

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && toggle.getAttribute("aria-expanded") === "true") {
        setOpen(false);
        toggle.focus();
      }
    });

    // Following a link inside the panel should close it.
    nav.addEventListener("click", function (e) {
      if (e.target.closest("a")) setOpen(false);
    });

    // Returning to the desktop layout must not leave the panel stuck open.
    var wide = window.matchMedia("(min-width: 901px)");
    var sync = function () { if (wide.matches) setOpen(false); };
    if (wide.addEventListener) wide.addEventListener("change", sync);
    else if (wide.addListener) wide.addListener(sync);
  }

  /* Footer year ------------------------------------------------------------ */
  var year = document.querySelector("[data-year]");
  if (year) year.textContent = String(new Date().getFullYear());

  /* ------------------------------------------------------------------------
     Scroll reveal

     The selector list mirrors the one in site.css that sets the hidden start
     state. If you add a target in one place, add it in the other. */
  var REVEAL = [
    ".hero__copy > *", ".hero__figure", ".stats > .stat",
    ".sec-head", ".sec-more", ".split__r",
    ".grid > .card", ".grid > .feature", ".grid > .tile", ".caps > a",
    ".steps > .step", ".projects > .project", ".facts > .facts__row",
    ".callout", ".photo-slot", ".faq > .faq__item", ".band__inner > *",
    ".aside > .aside__card", ".prose > h2", ".prose > .pull",
    ".form > .field", ".form > .form__row", ".form > .field--radios",
    ".contact-list > li"
  ].join(",");

  var targets = Array.prototype.slice.call(document.querySelectorAll(REVEAL));

  /* Anything still waiting to be revealed. Kept so a jump that skips past
     content can be swept up — see sweepPending below. */
  var pending = [];
  var io = null;

  var show = function (el) {
    el.classList.add("is-in");
    if (io) io.unobserve(el);
    var at = pending.indexOf(el);
    if (at !== -1) pending.splice(at, 1);
  };

  /* A jump rather than a scroll — End, a deep anchor, a restored position —
     moves content from below the viewport to above it between two frames.
     The observer never sees it intersect, so those elements would stay at
     opacity 0 for good. Anything at or above the fold gets revealed outright. */
  var sweepPending = function () {
    var h = window.innerHeight;
    pending.slice().forEach(function (el) {
      if (el.getBoundingClientRect().top < h) show(el);
    });
  };

  if (!targets.length) {
    /* nothing to do */
  } else if (reduced || !("IntersectionObserver" in window)) {
    targets.forEach(function (el) { el.classList.add("is-in"); });
  } else {
    /* Stagger is per parent, so a four-card row cascades but two unrelated
       blocks on the same screen do not wait on each other. */
    var seen = new Map();
    targets.forEach(function (el) {
      var parent = el.parentNode;
      var i = seen.has(parent) ? seen.get(parent) + 1 : 0;
      seen.set(parent, i);
      if (i) el.style.setProperty("--d", Math.min(i, 7) * 65 + "ms");
    });

    pending = targets.slice();

    io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        // `top < 0` catches a page that loaded already scrolled past this
        // element, where there is no intersection change left to wait for.
        if (entry.isIntersecting || entry.boundingClientRect.top < 0) show(entry.target);
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });

    targets.forEach(function (el) { io.observe(el); });
  }

  /* ------------------------------------------------------------------------
     Counting stats

     Only values shaped like "20+", "100%" or "48h" animate. Anything with two
     numbers in it — "24/7" — is left exactly as authored. */
  var stats = document.querySelectorAll(".stat__v");

  if (stats.length && !reduced && "IntersectionObserver" in window) {
    var countIO = new IntersectionObserver(function (entries, obs) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        obs.unobserve(entry.target);
        countUp(entry.target);
      });
    }, { threshold: 0.6 });

    Array.prototype.forEach.call(stats, function (el) {
      if (/^\D*\d+\D*$/.test(el.textContent.trim())) countIO.observe(el);
    });
  }

  function countUp(el) {
    var text = el.textContent.trim();
    var m = text.match(/^(\D*)(\d+)(\D*)$/);
    if (!m) return;

    var pre = m[1], target = parseInt(m[2], 10), post = m[3];
    var dur = 1100, start = null;

    el.style.minWidth = el.offsetWidth + "px";

    var tick = function (now) {
      if (start === null) start = now;
      var p = Math.min((now - start) / dur, 1);
      // Ease-out cubic: fast off the mark, settles rather than stops.
      var v = Math.round(target * (1 - Math.pow(1 - p, 3)));
      el.textContent = pre + v + post;
      if (p < 1) requestAnimationFrame(tick);
      else { el.textContent = text; el.style.minWidth = ""; }
    };
    requestAnimationFrame(tick);
  }

  /* ------------------------------------------------------------------------
     The single-line diagram energises when it comes into view. */
  var sld = document.querySelector(".sld");
  if (sld && !reduced) {
    if ("IntersectionObserver" in window) {
      var sldIO = new IntersectionObserver(function (entries, obs) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("is-live");
          obs.unobserve(entry.target);
        });
      }, { threshold: 0.25 });
      sldIO.observe(sld);
    } else {
      sld.classList.add("is-live");
    }
  }

  /* ------------------------------------------------------------------------
     Header state and reading progress.

     Both read the same scroll position, so they share one rAF-throttled
     handler rather than fighting over frames. */
  var header = document.querySelector(".site-header");
  var progress = null;

  if (header) {
    progress = document.createElement("div");
    progress.className = "scroll-progress";
    progress.setAttribute("aria-hidden", "true");
    header.appendChild(progress);
  }

  /* Back to top ------------------------------------------------------------ */
  var toTop = document.createElement("button");
  toTop.type = "button";
  toTop.className = "to-top";
  toTop.setAttribute("data-show", "false");
  toTop.setAttribute("aria-label", EL ? "Επιστροφή στην κορυφή" : "Back to top");
  toTop.innerHTML =
    '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false" fill="none" ' +
    'stroke="currentColor" stroke-width="2" stroke-linecap="round" ' +
    'stroke-linejoin="round"><path d="M12 19V5"/><path d="M5 12l7-7 7 7"/></svg>';
  toTop.addEventListener("click", function () {
    window.scrollTo({ top: 0, behavior: reduced ? "auto" : "smooth" });
  });
  document.body.appendChild(toTop);

  var ticking = false;
  var lastY = window.pageYOffset || root.scrollTop || 0;

  var onScroll = function () {
    var y = window.pageYOffset || root.scrollTop || 0;

    // Only sweep after a jump. Ordinary scrolling is the observer's job.
    if (pending.length && Math.abs(y - lastY) > window.innerHeight) sweepPending();
    lastY = y;

    document.body.classList.toggle("is-scrolled", y > 24);
    toTop.setAttribute("data-show", String(y > 700));

    if (progress) {
      var span = (root.scrollHeight - window.innerHeight) || 1;
      progress.style.setProperty("--p", Math.min(y / span, 1).toFixed(4));
    }
    ticking = false;
  };

  window.addEventListener("scroll", function () {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(onScroll);
  }, { passive: true });

  window.addEventListener("resize", onScroll, { passive: true });
  onScroll();

  /* ------------------------------------------------------------------------
     FAQ panels

     <details> gives us the correct semantics and the no-JS behaviour; this
     only adds the height transition browsers still will not do for us. The
     element is left fully native if the Web Animations API is missing or the
     visitor asked for reduced motion. */
  if (!reduced && typeof Element.prototype.animate === "function") {
    Array.prototype.forEach.call(
      document.querySelectorAll("details.faq__item"),
      function (item) {
        var summary = item.querySelector("summary");
        var panel = item.querySelector(".faq__a");
        if (!summary || !panel) return;

        var running = null;   // the height animation, which owns the sequence
        var fading = null;    // the answer's cross-fade, slaved to it

        var stop = function () {
          if (running) {
            // Drop the handlers before cancelling, or the interrupted run
            // would restore the open state this click is replacing.
            running.onfinish = running.oncancel = null;
            running.cancel();
            running = null;
          }
          if (fading) { fading.cancel(); fading = null; }
        };

        summary.addEventListener("click", function (e) {
          e.preventDefault();

          var opening = !item.open;
          var from = item.offsetHeight;

          stop();
          item.setAttribute("data-animating", "");

          // Measure the end state by actually being in it. Staying open for
          // the duration is also what lets the panel animate on the way out.
          item.open = true;
          var to = opening ? item.offsetHeight : summary.offsetHeight;

          running = item.animate(
            { height: [from + "px", to + "px"] },
            { duration: 280, easing: EASE }
          );
          // fill:"both" matters — without it the fade-out would release at its
          // own end and flash the answer back in while the panel is still
          // collapsing. It is cancelled below once the sequence is over.
          fading = panel.animate(
            { opacity: opening ? [0, 1] : [1, 0] },
            { duration: 280, easing: "ease", fill: "both" }
          );

          running.onfinish = running.oncancel = function () {
            item.open = opening;
            item.removeAttribute("data-animating");
            if (fading) { fading.cancel(); fading = null; }
            running = null;
          };
        });
      }
    );
  }
})();
