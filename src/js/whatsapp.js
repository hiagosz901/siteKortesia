(function () {
  function getConfig() {
    return window.SITE_CONFIG || {};
  }

  function createWhatsAppLink(message) {
    const config = getConfig();
    const base = 'https://wa.me/' + config.whatsappNumber;
    const text = message || config.defaultWhatsappMessage;

    return text ? base + '?text=' + encodeURIComponent(text) : base;
  }

  function applyContactLinks(root = document) {
    const config = getConfig();

    root.querySelectorAll('[data-whatsapp-message]').forEach((link) => {
      const message = link.getAttribute('data-whatsapp-message') || '';
      link.href = createWhatsAppLink(message);
    });

    root.querySelectorAll('[data-phone-link]').forEach((link) => {
      link.href = 'tel:' + config.phoneHref;
    });

    root.querySelectorAll('[data-phone-display]').forEach((element) => {
      element.textContent = config.phoneDisplay;
    });

    root.querySelectorAll('[data-phone-placeholder]').forEach((element) => {
      element.placeholder = config.phoneDisplay;
    });
  }

  window.KortesiaWhatsApp = {
    createWhatsAppLink,
    applyContactLinks
  };
})();
