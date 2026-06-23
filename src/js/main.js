(function () {
  function hasDependencies() {
    return Boolean(
      window.KortesiaWhatsApp &&
      window.KortesiaMenu &&
      window.KortesiaFaq &&
      window.KortesiaScroll &&
      window.KortesiaForm
    );
  }

  function initSite() {
    if (window.__KORTESIA_INITIALIZED__ || !hasDependencies()) {
      return;
    }

    window.__KORTESIA_INITIALIZED__ = true;

    window.KortesiaWhatsApp.applyContactLinks();

    const closeMenu = window.KortesiaMenu.initMenu();

    window.KortesiaFaq.initFaq();
    window.KortesiaScroll.initRevealAnimations();
    window.KortesiaScroll.initHeaderScroll();
    window.KortesiaScroll.initSmoothScroll(closeMenu);
    window.KortesiaForm.initContactForm();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initSite);
    return;
  }

  initSite();
})();
