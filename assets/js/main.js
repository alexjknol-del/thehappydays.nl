/* The Happy Days — kleine, afhankelijkheidsvrije interacties */
(function () {
  "use strict";

  /* ---- Sticky header schaduw bij scrollen ---- */
  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () {
      header.classList.toggle("is-scrolled", window.scrollY > 8);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* ---- Mobiel menu openen/sluiten ---- */
  var burger = document.querySelector(".nav__burger");
  var links = document.getElementById("primary-nav");
  if (burger && links) {
    burger.addEventListener("click", function () {
      var open = links.classList.toggle("is-open");
      burger.setAttribute("aria-expanded", open ? "true" : "false");
      document.body.style.overflow = open && window.innerWidth <= 720 ? "hidden" : "";
    });
    // Sluit bij klik op een echte link
    links.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        links.classList.remove("is-open");
        burger.setAttribute("aria-expanded", "false");
        document.body.style.overflow = "";
      });
    });
  }

  /* ---- Submenu (Nieuws ▾) — klik/toets op mobiel, hover op desktop ---- */
  document.querySelectorAll(".nav__toggle-sub").forEach(function (btn) {
    var sub = btn.parentElement.querySelector(".submenu");
    btn.addEventListener("click", function (e) {
      // Op desktop opent hover het al; alleen op smal scherm togglen we
      if (window.innerWidth <= 720) {
        e.preventDefault();
        var open = sub.classList.toggle("is-open");
        btn.setAttribute("aria-expanded", open ? "true" : "false");
      }
    });
  });

  /* ---- Sluit menu's met Escape ---- */
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && links && links.classList.contains("is-open")) {
      links.classList.remove("is-open");
      if (burger) {
        burger.setAttribute("aria-expanded", "false");
        burger.focus();
      }
      document.body.style.overflow = "";
    }
  });

  /* ---- Cookiemelding (alleen functionele opslag) ---- */
  var bar = document.getElementById("cookiebar");
  if (bar) {
    var KEY = "thd-cookie-ack";
    var stored = null;
    try { stored = window.localStorage.getItem(KEY); } catch (err) { stored = null; }
    if (!stored) {
      window.setTimeout(function () { bar.classList.add("is-visible"); }, 700);
    }
    bar.querySelectorAll("[data-cookie-accept]").forEach(function (b) {
      b.addEventListener("click", function () {
        try { window.localStorage.setItem(KEY, "1"); } catch (err) {}
        bar.classList.remove("is-visible");
      });
    });
  }

  /* ---- Jaartal in de footer ---- */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
