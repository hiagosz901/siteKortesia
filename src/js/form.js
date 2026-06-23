(function () {
  function initContactForm() {
    const form = document.getElementById('contactForm');

    if (!form) {
      return;
    }

    const fields = {
      nome: document.getElementById('nome'),
      tel: document.getElementById('tel'),
      bairro: document.getElementById('bairro'),
      problema: document.getElementById('problema'),
      msg: document.getElementById('msg')
    };

    form.addEventListener('submit', (event) => {
      event.preventDefault();

      const nome = fields.nome?.value.trim() || '';
      const tel = fields.tel?.value.trim() || '';
      const bairro = fields.bairro?.value.trim() || '';
      const problema = fields.problema?.value || '';
      const msg = fields.msg?.value.trim() || '';

      [fields.nome, fields.tel].forEach((field) => {
        field?.removeAttribute('aria-invalid');
      });

      if (!nome || !tel) {
        if (!nome) fields.nome?.setAttribute('aria-invalid', 'true');
        if (!tel) fields.tel?.setAttribute('aria-invalid', 'true');
        alert('Por favor, preencha pelo menos seu nome e telefone.');
        return;
      }

      const lines = [
        '*Novo contato pelo site*',
        '\u{1F464} *Nome:* ' + nome,
        '\u{1F4DE} *Telefone:* ' + tel,
        bairro ? '\u{1F4CD} *Bairro:* ' + bairro : '',
        problema ? '\u{1F527} *Servi\u00E7o:* ' + problema : '',
        msg ? '\u{1F4DD} *Mensagem:* ' + msg : ''
      ].filter(Boolean).join('\n');

      window.open(window.KortesiaWhatsApp.createWhatsAppLink(lines), '_blank', 'noopener');
    });
  }

  window.KortesiaForm = { initContactForm };
})();
