(function () {
  function initFaq() {
    document.querySelectorAll('.faq-q').forEach((button) => {
      button.addEventListener('click', () => {
        const item = button.closest('.faq-item');

        if (!item) {
          return;
        }

        const isOpen = item.classList.toggle('open');
        button.setAttribute('aria-expanded', String(isOpen));
      });
    });
  }

  window.KortesiaFaq = { initFaq };
})();
