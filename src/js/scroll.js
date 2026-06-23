(function () {
  const HEADER_OFFSET = 76;

  function initRevealAnimations() {
    const elements = document.querySelectorAll('.reveal');

    if (!('IntersectionObserver' in window)) {
      elements.forEach((element) => element.classList.add('visible'));
      return;
    }

    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });

    elements.forEach((element) => observer.observe(element));
  }

  function initHeaderScroll() {
    const header = document.getElementById('header');

    if (!header) {
      return;
    }

    function updateHeader() {
      header.classList.toggle('is-scrolled', window.scrollY > 10);
    }

    updateHeader();
    window.addEventListener('scroll', updateHeader, { passive: true });
  }

  function initSmoothScroll(closeMenu = function closeNoop() {}) {
    document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
      anchor.addEventListener('click', (event) => {
        const href = anchor.getAttribute('href');

        if (!href || href === '#') {
          return;
        }

        const target = document.querySelector(href);

        if (!target) {
          return;
        }

        event.preventDefault();
        const top = target.getBoundingClientRect().top + window.scrollY - HEADER_OFFSET;
        window.scrollTo({ top, behavior: 'smooth' });
        closeMenu();
      });
    });
  }

  window.KortesiaScroll = {
    initRevealAnimations,
    initHeaderScroll,
    initSmoothScroll
  };
})();
