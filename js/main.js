/* Samarth Dental Clinic — site interactions */
(function () {
  "use strict";

  var WHATSAPP = "916355964694";

  /* ---------------------------------------------------------------- helpers */
  function $(sel, root) { return (root || document).querySelector(sel); }
  function $$(sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); }

  /* ------------------------------------------------- header scroll + to-top */
  var header = $(".site-header");
  var toTop = $(".float-top");

  function onScroll() {
    var y = window.scrollY;
    if (header) header.classList.toggle("is-scrolled", y > 10);
    if (toTop) toTop.classList.toggle("show", y > 600);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  if (toTop) {
    toTop.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  /* ------------------------------------------------------ mobile navigation */
  var nav = $(".nav");
  var toggle = $(".menu-toggle");
  var navClose = $(".nav-close");
  var backdrop = $(".nav-backdrop");

  function setNav(open) {
    if (!nav) return;
    nav.classList.toggle("open", open);
    document.body.classList.toggle("nav-open", open);
    if (backdrop) {
      backdrop.classList.toggle("show", open);
      backdrop.setAttribute("aria-hidden", open ? "false" : "true");
    }
    if (toggle) toggle.setAttribute("aria-expanded", open ? "true" : "false");
  }

  if (toggle) toggle.addEventListener("click", function () { setNav(!nav.classList.contains("open")); });
  if (navClose) navClose.addEventListener("click", function () { setNav(false); });
  if (backdrop) backdrop.addEventListener("click", function () { setNav(false); });

  document.addEventListener("keydown", function (e) {
    if (e.key !== "Escape") return;
    setNav(false);
    closeLightbox();
  });

  /* On narrow screens the Services parent toggles its submenu instead of navigating. */
  $$(".has-drop").forEach(function (group) {
    var trigger = $(".nav-link", group);
    if (!trigger) return;
    trigger.addEventListener("click", function (e) {
      if (!window.matchMedia("(max-width: 1024px)").matches) return;
      e.preventDefault();
      group.classList.toggle("open");
    });
  });

  /* -------------------------------------------------- mark the current page */
  var here = location.pathname.split("/").pop() || "index.html";
  $$(".nav .nav-link[href]").forEach(function (link) {
    if (link.getAttribute("href") === here) link.classList.add("active");
  });
  $$(".drop a[href]").forEach(function (link) {
    if (link.getAttribute("href") !== here) return;
    link.classList.add("active");
    var parent = link.closest(".has-drop");
    if (parent) $(".nav-link", parent).classList.add("active");
  });
  $$(".side-nav a[href]").forEach(function (link) {
    if (link.getAttribute("href") === here) link.classList.add("active");
  });

  /* ------------------------------------------------------------ footer year */
  $$("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* ---------------------------------------------------------- scroll reveal
     Deliberately measured from scroll position rather than IntersectionObserver.
     The effect is decorative, but the content it hides is not, so it must never
     be possible for an element to stay hidden. */
  var revealables = $$("[data-reveal]");

  function reveal() {
    var limit = window.innerHeight - 60;
    revealables = revealables.filter(function (el) {
      if (el.getBoundingClientRect().top > limit) return true;
      el.style.transitionDelay = (el.getAttribute("data-reveal-delay") || 0) + "ms";
      el.classList.add("in");
      return false;
    });
    if (!revealables.length) {
      window.removeEventListener("scroll", reveal);
      window.removeEventListener("resize", reveal);
    }
  }

  if (revealables.length) {
    window.addEventListener("scroll", reveal, { passive: true });
    window.addEventListener("resize", reveal);
    window.addEventListener("load", reveal);
    reveal();
  }

  /* --------------------------------------------------------------- counters
     The markup already carries the final figure, so a counter that never
     animates still reads correctly. */
  var counters = $$("[data-count]");

  function tickCounters() {
    var limit = window.innerHeight - 40;
    counters = counters.filter(function (el) {
      if (el.getBoundingClientRect().top > limit) return true;
      runCount(el);
      return false;
    });
    if (!counters.length) window.removeEventListener("scroll", tickCounters);
  }

  if (counters.length) {
    window.addEventListener("scroll", tickCounters, { passive: true });
    window.addEventListener("load", tickCounters);
    tickCounters();
  }

  function runCount(el) {
    var target = parseFloat(el.getAttribute("data-count"));
    var decimals = (el.getAttribute("data-count").split(".")[1] || "").length;
    var suffix = el.getAttribute("data-suffix") || "";
    var duration = 1500;
    var start = performance.now();

    function frame(now) {
      var progress = Math.min((now - start) / duration, 1);
      var eased = 1 - Math.pow(1 - progress, 3);
      el.textContent = (target * eased).toFixed(decimals) + suffix;
      if (progress < 1) requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);
  }

  /* ----------------------------------------------------------- testimonials */
  $$("[data-slider]").forEach(function (slider) {
    var track = $(".slider-track", slider);
    var slides = $$(".slide", track);
    var prev = $("[data-slider-prev]", slider);
    var next = $("[data-slider-next]", slider);
    if (!track || !slides.length) return;

    var index = 0;

    function perView() {
      if (window.matchMedia("(max-width: 760px)").matches) return 1;
      if (window.matchMedia("(max-width: 1024px)").matches) return 2;
      return 3;
    }

    function maxIndex() { return Math.max(0, slides.length - perView()); }

    function render() {
      index = Math.min(index, maxIndex());
      var step = 100 / perView();
      track.style.transform = "translateX(-" + index * step + "%)";
      slides.forEach(function (slide, i) {
        var visible = i >= index && i < index + perView();
        slide.setAttribute("aria-hidden", visible ? "false" : "true");
      });
      if (prev) prev.disabled = index === 0;
      if (next) next.disabled = index >= maxIndex();
    }

    slides.forEach(function (slide) { slide.style.flexBasis = ""; });
    if (prev) prev.addEventListener("click", function () { index = Math.max(0, index - 1); render(); });
    if (next) next.addEventListener("click", function () { index = Math.min(maxIndex(), index + 1); render(); });

    /* Touch swipe */
    var startX = null;
    track.addEventListener("touchstart", function (e) { startX = e.touches[0].clientX; }, { passive: true });
    track.addEventListener("touchend", function (e) {
      if (startX === null) return;
      var delta = e.changedTouches[0].clientX - startX;
      if (Math.abs(delta) > 45) {
        index = delta < 0 ? Math.min(maxIndex(), index + 1) : Math.max(0, index - 1);
        render();
      }
      startX = null;
    }, { passive: true });

    window.addEventListener("resize", render);
    render();
  });

  /* -------------------------------------------------------------- accordion */
  $$(".accordion").forEach(function (accordion) {
    var items = $$(".ac-item", accordion);
    items.forEach(function (item) {
      var head = $(".ac-head", item);
      if (!head) return;
      head.addEventListener("click", function () {
        var isOpen = item.classList.contains("open");
        items.forEach(function (other) {
          other.classList.remove("open");
          var h = $(".ac-head", other);
          if (h) h.setAttribute("aria-expanded", "false");
        });
        if (!isOpen) {
          item.classList.add("open");
          head.setAttribute("aria-expanded", "true");
        }
      });
    });
  });

  /* --------------------------------------------------------------- lightbox */
  var lightbox = $(".lightbox");
  var lightboxImg = lightbox ? $("img", lightbox) : null;
  var lightboxCap = lightbox ? $(".lightbox-caption", lightbox) : null;

  function closeLightbox() {
    if (!lightbox) return;
    lightbox.classList.remove("open");
    document.body.style.overflow = "";
  }

  $$("[data-lightbox]").forEach(function (item) {
    item.addEventListener("click", function (e) {
      if (!lightbox || !lightboxImg) return;
      e.preventDefault();
      var img = $("img", item);
      lightboxImg.src = item.getAttribute("data-lightbox") || (img && img.src) || "";
      lightboxImg.alt = (img && img.alt) || "";
      if (lightboxCap) lightboxCap.textContent = (img && img.alt) || "";
      lightbox.classList.add("open");
      document.body.style.overflow = "hidden";
    });
  });

  if (lightbox) {
    lightbox.addEventListener("click", function (e) {
      if (e.target === lightbox || e.target.classList.contains("lightbox-close")) closeLightbox();
    });
  }

  /* ------------------------------------------------------------------ forms
     There is no backend, so a validated submission is handed to WhatsApp with
     the enquiry pre-written. The on-page confirmation stays visible either way. */
  $$("[data-form]").forEach(function (form) {
    var alertBox = $(".form-alert", form);

    form.addEventListener("submit", function (e) {
      e.preventDefault();

      if (!form.checkValidity()) {
        form.reportValidity();
        return;
      }

      var data = new FormData(form);
      var lines = [form.getAttribute("data-form-title") || "New enquiry from website"];
      data.forEach(function (value, key) {
        if (String(value).trim()) lines.push(key + ": " + value);
      });

      var url = "https://wa.me/" + WHATSAPP + "?text=" + encodeURIComponent(lines.join("\n"));
      window.open(url, "_blank", "noopener");

      if (alertBox) {
        alertBox.classList.add("show");
        alertBox.scrollIntoView({ behavior: "smooth", block: "center" });
      }
      form.reset();
    });
  });

  /* Appointment date pickers should not accept past dates. */
  $$("input[type='date']").forEach(function (input) {
    if (!input.min) input.min = new Date().toISOString().split("T")[0];
  });
})();
