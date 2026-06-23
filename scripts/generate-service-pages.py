# -*- coding: utf-8 -*-
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = ROOT / "pages"

WA_SVG = '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>'
PHONE_SVG = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 9.81 19.79 19.79 0 01.1 1.18 2 2 0 012.08 0h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.91 7.09a16 16 0 006 6l.45-.45a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 16.92z"/></svg>'

SERVICES = [
    {
        "file": "desentupimento-vaso",
        "title": "Desentupimento de Vaso | Kortesia Desentupidora",
        "meta": "Desentupimento de vaso sanit&aacute;rio com equipamentos profissionais. Atendimento r&aacute;pido, sem sujeira e 24h em S&atilde;o Paulo.",
        "badge": "Desentupimento Profissional",
        "h1": "Desentupimento de Vaso",
        "h1_span": "R&aacute;pido e Sem Sujeira",
        "desc": "Desentupimento de vasos sanit&aacute;rios com equipamentos profissionais. Atendemos resid&ecirc;ncias, com&eacute;rcios e condom&iacute;nios em S&atilde;o Paulo e regi&atilde;o, 24 horas por dia.",
        "checklist": ["Atendimento em at&eacute; 30 minutos", "Equipamentos de alta press&atilde;o", "Sem quebra de parede ou piso", "Or&ccedil;amento gratuito no local", "T&eacute;cnicos uniformizados e identificados"],
        "wa": "Ol&aacute;! Preciso de desentupimento de vaso sanit&aacute;rio.",
        "wa_cta": "Ol&aacute;! Preciso de desentupimento de vaso agora!",
        "img": "desentupimento-vaso.png",
        "img_alt": "T&eacute;cnico realizando desentupimento de vaso sanit&aacute;rio",
        "card_title": "Desentupimento de Vaso Sanit&aacute;rio",
        "card_desc": "Utilizamos equipamentos de alta press&atilde;o e sondas flex&iacute;veis para desobstruir qualquer tipo de entupimento sem danos &agrave; lou&ccedil;a.",
        "tags": ["Residencial", "Comercial", "Condom&iacute;nio", "Sem quebra", "24 horas"],
        "faq_title": "Perguntas frequentes sobre desentupimento de vaso",
        "faqs": [
            ("Voc&ecirc;s atendem de madrugada?", "Sim! Nosso atendimento &eacute; 24 horas, 7 dias por semana, incluindo madrugadas, fins de semana e feriados."),
            ("V&atilde;o precisar quebrar o piso ou parede?", "Na grande maioria dos casos, n&atilde;o. Utilizamos sondas e equipamentos que resolvem o entupimento sem obras."),
            ("Quanto tempo demora o atendimento?", "Nosso t&eacute;cnico chega em m&eacute;dia em 30 minutos. O servi&ccedil;o costuma ser resolvido em 1 a 2 horas."),
            ("Quais formas de pagamento voc&ecirc;s aceitam?", "Aceitamos dinheiro, Pix, cart&atilde;o de d&eacute;bito e cr&eacute;dito. Pagamento ap&oacute;s a conclus&atilde;o do servi&ccedil;o."),
        ],
        "cta_h2": "Vaso entupido? A gente resolve agora.",
        "cta_p": "T&eacute;cnicos dispon&iacute;veis em toda S&atilde;o Paulo e regi&atilde;o metropolitana. Atendimento imediato.",
    },
    {
        "file": "desentupimento-pia",
        "title": "Desentupimento de Pia | Kortesia Desentupidora",
        "meta": "Desobstru&ccedil;&atilde;o de pias de cozinha e banheiro. Removemos gordura, res&iacute;duos e obstru&ccedil;&otilde;es em S&atilde;o Paulo.",
        "badge": "Desentupimento de Pia",
        "h1": "Desentupimento de Pia",
        "h1_span": "Cozinha e Banheiro",
        "desc": "Desobstru&ccedil;&atilde;o de pias de cozinha e banheiro. Removemos gordura, res&iacute;duos e obstru&ccedil;&otilde;es com efici&ecirc;ncia e equipamentos adequados.",
        "checklist": ["Pias de cozinha e banheiro", "Remo&ccedil;&atilde;o de gordura acumulada", "Escoamento normalizado", "Or&ccedil;amento antes do servi&ccedil;o", "Atendimento 24h"],
        "wa": "Ol&aacute;! Preciso de desentupimento de pia.",
        "wa_cta": "Ol&aacute;! Preciso de desentupimento de pia agora!",
        "img": "desentupimento-pia.png",
        "img_alt": "T&eacute;cnico desentupindo pia de cozinha",
        "card_title": "Desentupimento de Pia",
        "card_desc": "Limpeza profunda de sif&atilde;o e tubula&ccedil;&atilde;o para eliminar gordura, restos de alimentos e obstru&ccedil;&otilde;es.",
        "tags": ["Cozinha", "Banheiro", "Restaurantes", "Sem quebra", "24 horas"],
        "faq_title": "Perguntas frequentes sobre desentupimento de pia",
        "faqs": [
            ("Serve para pia de cozinha e banheiro?", "Sim. Atendemos ambos com equipamentos adequados para cada situa&ccedil;&atilde;o."),
            ("Produtos caseiros n&atilde;o resolveram?", "Se a pia continua lenta, chame um t&eacute;cnico para evitar piora na tubula&ccedil;&atilde;o."),
            ("Quanto custa?", "O valor depende do tipo de obstru&ccedil;&atilde;o. Solicite um or&ccedil;amento sem compromisso."),
            ("Atende com&eacute;rcio?", "Sim. Cozinhas comerciais e restaurantes s&atilde;o atendidos com equipamento refor&ccedil;ado."),
        ],
        "cta_h2": "Pia entupida? Solicite or&ccedil;amento agora.",
        "cta_p": "Atendimento r&aacute;pido em S&atilde;o Paulo para pias de cozinha e banheiro.",
    },
    {
        "file": "desentupimento-ralo",
        "title": "Desentupimento de Ralo | Kortesia Desentupidora",
        "meta": "Limpeza e desentupimento de ralos com elimina&ccedil;&atilde;o de mau cheiro e melhora no escoamento em S&atilde;o Paulo.",
        "badge": "Desentupimento de Ralo",
        "h1": "Desentupimento de Ralo",
        "h1_span": "Sem Mau Cheiro",
        "desc": "Limpeza e desentupimento de ralos de box, cozinha e &aacute;rea externa. Eliminamos mau cheiro e melhoramos o escoamento da &aacute;gua.",
        "checklist": ["Ralos de box e piso", "&Aacute;reas externas e garagem", "Elimina&ccedil;&atilde;o de mau cheiro", "Equipamentos compactos", "Atendimento emergencial"],
        "wa": "Ol&aacute;! Preciso de desentupimento de ralo.",
        "wa_cta": "Ol&aacute;! Preciso de desentupimento de ralo agora!",
        "img": "desentupimento-ralo.png",
        "img_alt": "Desentupimento de ralo com equipamento profissional",
        "card_title": "Desentupimento de Ralo",
        "card_desc": "Removemos cabelo, sab&atilde;o, lodo e res&iacute;duos que causam entupimento e odor nos ralos.",
        "tags": ["Box", "Cozinha", "Externa", "Condom&iacute;nio", "24 horas"],
        "faq_title": "Perguntas frequentes sobre desentupimento de ralo",
        "faqs": [
            ("Mau cheiro pode ser entupimento?", "Sim. Ac&uacute;mulo de res&iacute;duos no ralo e sif&atilde;o &eacute; causa comum de odor."),
            ("Precisa trocar o ralo?", "Na maioria dos casos a limpeza resolve. Troca s&oacute; se houver dano."),
            ("Atende &aacute;rea externa?", "Sim. Ralos de quintal, garagem e varanda tamb&eacute;m s&atilde;o atendidos."),
            ("Quanto tempo leva?", "A maioria dos casos &eacute; resolvida em uma &uacute;nica visita."),
        ],
        "cta_h2": "Ralo entupido ou com mau cheiro?",
        "cta_p": "Chame agora e receba or&ccedil;amento para desentupimento de ralo em S&atilde;o Paulo.",
    },
    {
        "file": "desentupimento-esgoto",
        "title": "Desentupimento de Esgoto | Kortesia Desentupidora",
        "meta": "Desobstru&ccedil;&atilde;o de tubula&ccedil;&otilde;es de esgoto residenciais, comerciais e condominiais em S&atilde;o Paulo.",
        "badge": "Desentupimento de Esgoto",
        "h1": "Desentupimento de Esgoto",
        "h1_span": "Sem Retorno",
        "desc": "Desobstru&ccedil;&atilde;o de tubula&ccedil;&otilde;es de esgoto residenciais, comerciais e condominiais. Preven&ccedil;&atilde;o de retorno de dejetos.",
        "checklist": ["Retorno de esgoto", "M&aacute;quinas rotativas e suc&ccedil;&atilde;o", "Condom&iacute;nios e pr&eacute;dios", "Diagn&oacute;stico t&eacute;cnico", "Atendimento 24h"],
        "wa": "Ol&aacute;! Preciso de desentupimento de esgoto.",
        "wa_cta": "Ol&aacute;! Preciso de desentupimento de esgoto urgente!",
        "img": "desentupimento-esgoto.png",
        "img_alt": "Desentupimento de rede de esgoto",
        "card_title": "Desentupimento de Esgoto",
        "card_desc": "Equipamentos de alta performance para desobstruir colunas, prumadas e redes coletivas de esgoto.",
        "tags": ["Residencial", "Condom&iacute;nio", "Comercial", "Colunas", "24 horas"],
        "faq_title": "Perguntas frequentes sobre desentupimento de esgoto",
        "faqs": [
            ("Esgoto voltou, o que fazer?", "Evite usar vasos e ralos e chame atendimento imediato."),
            ("Precisa de hidrojateamento?", "Em obstru&ccedil;&otilde;es severas, o hidrojateamento pode ser recomendado."),
            ("Atende pr&eacute;dios?", "Sim. Resid&ecirc;ncias, com&eacute;rcios e condom&iacute;nios."),
            ("Tem or&ccedil;amento?", "Sim. Or&ccedil;amento claro antes de iniciar o servi&ccedil;o."),
        ],
        "cta_h2": "Esgoto voltando? Atendimento imediato.",
        "cta_p": "Equipe preparada para casos urgentes de retorno de esgoto em S&atilde;o Paulo.",
    },
    {
        "file": "caca-vazamento",
        "title": "Ca&ccedil;a Vazamento | Kortesia Desentupidora",
        "meta": "Localiza&ccedil;&atilde;o de vazamentos ocultos com geofone e equipamentos t&eacute;cnicos em S&atilde;o Paulo.",
        "badge": "Ca&ccedil;a Vazamento",
        "h1": "Ca&ccedil;a Vazamento",
        "h1_span": "Sem Quebradeira",
        "desc": "Detec&ccedil;&atilde;o de vazamentos ocultos com geofone e equipamentos t&eacute;cnicos. Reduzimos quebras desnecess&aacute;rias quando poss&iacute;vel.",
        "checklist": ["Geofone e equipamentos t&eacute;cnicos", "Conta de &aacute;gua alta", "Infiltra&ccedil;&atilde;o e umidade", "Laudo t&eacute;cnico se aplic&aacute;vel", "Atendimento 24h"],
        "wa": "Ol&aacute;! Preciso de ca&ccedil;a vazamento em S&atilde;o Paulo.",
        "wa_cta": "Ol&aacute;! Preciso de ca&ccedil;a vazamento urgente!",
        "img": "caca-vazamento.png",
        "img_alt": "T&eacute;cnico realizando ca&ccedil;a vazamento",
        "card_title": "Ca&ccedil;a Vazamento",
        "card_desc": "Localizamos vazamentos ocultos em tubula&ccedil;&otilde;es, paredes e pisos com precis&atilde;o t&eacute;cnica.",
        "tags": ["Residencial", "Comercial", "Condom&iacute;nio", "Sem quebra", "Laudo"],
        "faq_title": "Perguntas frequentes sobre ca&ccedil;a vazamento",
        "faqs": [
            ("Precisa quebrar tudo?", "N&atilde;o necessariamente. A detec&ccedil;&atilde;o localiza o ponto exato do vazamento."),
            ("Conta de &aacute;gua alta indica vazamento?", "Sim. &Eacute; um dos sinais mais comuns de vazamento oculto."),
            ("Atende condom&iacute;nios?", "Sim. Residencial, comercial e condominial."),
            ("Emite laudo?", "Quando necess&aacute;rio, o registro t&eacute;cnico pode apoiar laudos."),
        ],
        "cta_h2": "Suspeita de vazamento oculto?",
        "cta_p": "Solicite or&ccedil;amento para ca&ccedil;a vazamento em S&atilde;o Paulo.",
    },
    {
        "file": "hidrojateamento",
        "title": "Hidrojateamento | Kortesia Desentupidora",
        "meta": "Limpeza de tubula&ccedil;&otilde;es, caixas de gordura e esgoto com alta press&atilde;o em S&atilde;o Paulo.",
        "badge": "Hidrojateamento",
        "h1": "Hidrojateamento",
        "h1_span": "Alta Press&atilde;o",
        "desc": "Limpeza de tubula&ccedil;&otilde;es, caixas de gordura e esgoto com alta press&atilde;o. Ideal para manuten&ccedil;&atilde;o preventiva e obstru&ccedil;&otilde;es severas.",
        "checklist": ["Alta press&atilde;o controlada", "Caixa de gordura", "Redes de esgoto", "Manuten&ccedil;&atilde;o preventiva", "Condom&iacute;nios e empresas"],
        "wa": "Ol&aacute;! Preciso de hidrojateamento em S&atilde;o Paulo.",
        "wa_cta": "Ol&aacute;! Preciso de hidrojateamento agora!",
        "img": "hidrojateamento.png",
        "img_alt": "Hidrojateamento de tubula&ccedil;&atilde;o",
        "card_title": "Hidrojateamento",
        "card_desc": "Remove incrusta&ccedil;&otilde;es, gordura e res&iacute;duos acumulados em tubula&ccedil;&otilde;es e caixas de gordura.",
        "tags": ["Caixa de gordura", "Esgoto", "Condom&iacute;nio", "Preventivo", "24 horas"],
        "faq_title": "Perguntas frequentes sobre hidrojateamento",
        "faqs": [
            ("Serve para caixa de gordura?", "Sim. &Eacute; uma das aplica&ccedil;&otilde;es mais comuns."),
            ("Pode ser preventivo?", "Sim. Condom&iacute;nios e com&eacute;rcios usam para reduzir entupimentos."),
            ("Atende empresas?", "Sim. Cozinhas, com&eacute;rcios e condom&iacute;nios."),
            ("Danifica a tubula&ccedil;&atilde;o?", "N&atilde;o. A press&atilde;o &eacute; controlada conforme o tipo de tubo."),
        ],
        "cta_h2": "Precisa de hidrojateamento?",
        "cta_p": "Or&ccedil;amento para limpeza de tubula&ccedil;&otilde;es e caixas de gordura em S&atilde;o Paulo.",
    },
    {
        "file": "video-inspecao",
        "title": "V&iacute;deo Inspe&ccedil;&atilde;o | Kortesia Desentupidora",
        "meta": "C&acirc;mera inspeciona tubula&ccedil;&otilde;es internamente com precis&atilde;o antes de qualquer interven&ccedil;&atilde;o em S&atilde;o Paulo.",
        "badge": "V&iacute;deo Inspe&ccedil;&atilde;o",
        "h1": "V&iacute;deo Inspe&ccedil;&atilde;o",
        "h1_span": "Diagn&oacute;stico Preciso",
        "desc": "C&acirc;mera inspeciona tubula&ccedil;&otilde;es internamente, identificando obstru&ccedil;&otilde;es, rupturas e pontos cr&iacute;ticos antes de qualquer interven&ccedil;&atilde;o.",
        "checklist": ["Diagn&oacute;stico antes de quebrar", "Registro em v&iacute;deo", "Casos recorrentes", "Laudo t&eacute;cnico", "Condom&iacute;nios e com&eacute;rcios"],
        "wa": "Ol&aacute;! Preciso de v&iacute;deo inspe&ccedil;&atilde;o de tubula&ccedil;&atilde;o.",
        "wa_cta": "Ol&aacute;! Preciso de v&iacute;deo inspe&ccedil;&atilde;o agora!",
        "img": "video-inspecao.png",
        "img_alt": "V&iacute;deo inspe&ccedil;&atilde;o de tubula&ccedil;&atilde;o com c&acirc;mera",
        "card_title": "V&iacute;deo Inspe&ccedil;&atilde;o",
        "card_desc": "Visualiza&ccedil;&atilde;o interna da tubula&ccedil;&atilde;o para localizar o problema com precis&atilde;o.",
        "tags": ["Diagn&oacute;stico", "Sem quebra", "Laudo", "Condom&iacute;nio", "24 horas"],
        "faq_title": "Perguntas frequentes sobre v&iacute;deo inspe&ccedil;&atilde;o",
        "faqs": [
            ("Para que serve a c&acirc;mera?", "Permite ver dentro da tubula&ccedil;&atilde;o e identificar obstru&ccedil;&otilde;es e rupturas."),
            ("Evita quebrar?", "Sim. Localiza o ponto exato do problema em muitos casos."),
            ("Gera laudo?", "Quando necess&aacute;rio, o registro apoia laudos e or&ccedil;amentos."),
            ("Quando &eacute; indicado?", "Entupimentos recorrentes, suspeita de ruptura ou manuten&ccedil;&atilde;o preventiva."),
        ],
        "cta_h2": "Precisa identificar o problema na tubula&ccedil;&atilde;o?",
        "cta_p": "Solicite or&ccedil;amento para v&iacute;deo inspe&ccedil;&atilde;o em S&atilde;o Paulo.",
    },
    {
        "file": "dedetizacao",
        "title": "Dedetiza&ccedil;&atilde;o | Kortesia Desentupidora",
        "meta": "Controle de baratas, ratos, formigas, cupins e outras pragas em S&atilde;o Paulo.",
        "badge": "Dedetiza&ccedil;&atilde;o e Pragas",
        "h1": "Dedetiza&ccedil;&atilde;o",
        "h1_span": "Controle de Pragas",
        "desc": "Controle de baratas, ratos, formigas, cupins e outros insetos. Produtos seguros para resid&ecirc;ncias, com&eacute;rcios e condom&iacute;nios.",
        "checklist": ["Produtos seguros e autorizados", "Baratas, ratos e formigas", "Plano conforme o ambiente", "Residencial e comercial", "Orienta&ccedil;&atilde;o p&oacute;s-aplica&ccedil;&atilde;o"],
        "wa": "Ol&aacute;! Preciso de dedetiza&ccedil;&atilde;o ou controle de pragas.",
        "wa_cta": "Ol&aacute;! Preciso de dedetiza&ccedil;&atilde;o agora!",
        "img": "dedetizacao.png",
        "img_alt": "Dedetiza&ccedil;&atilde;o e controle de pragas",
        "card_title": "Dedetiza&ccedil;&atilde;o",
        "card_desc": "Controle profissional de pragas urbanas com produtos autorizados e planejamento por ambiente.",
        "tags": ["Residencial", "Comercial", "Condom&iacute;nio", "Cupins", "Baratas"],
        "faq_title": "Perguntas frequentes sobre dedetiza&ccedil;&atilde;o",
        "faqs": [
            ("Os produtos s&atilde;o seguros?", "Sim. Utilizamos produtos autorizados e orientamos sobre reentrada."),
            ("Precisa sair de casa?", "Depende do tipo de aplica&ccedil;&atilde;o. A equipe orienta antes do servi&ccedil;o."),
            ("Atende com&eacute;rcio?", "Sim. Lojas, restaurantes e escrit&oacute;rios."),
            ("Tem garantia?", "Sim. Orientamos sobre recorr&ecirc;ncia e retorno se necess&aacute;rio."),
        ],
        "cta_h2": "Pragas em casa ou no com&eacute;rcio?",
        "cta_p": "Solicite or&ccedil;amento para dedetiza&ccedil;&atilde;o em S&atilde;o Paulo.",
    },
    {
        "file": "servicos-hidraulicos",
        "title": "Servi&ccedil;os Hidr&aacute;ulicos | Kortesia Desentupidora",
        "meta": "Reparos e instala&ccedil;&otilde;es hidr&aacute;ulicas: torneiras, registros, tubula&ccedil;&otilde;es e caixas d'&aacute;gua em S&atilde;o Paulo.",
        "badge": "Servi&ccedil;os Hidr&aacute;ulicos",
        "h1": "Servi&ccedil;os Hidr&aacute;ulicos",
        "h1_span": "Reparos e Instala&ccedil;&otilde;es",
        "desc": "Reparos e instala&ccedil;&otilde;es hidr&aacute;ulicas em geral: torneiras, registros, tubula&ccedil;&otilde;es, caixas d'&aacute;gua e muito mais.",
        "checklist": ["Torneiras e registros", "Instala&ccedil;&atilde;o de chuveiro", "Reparo de vazamentos", "Or&ccedil;amento claro", "Equipe qualificada"],
        "wa": "Ol&aacute;! Preciso de servi&ccedil;os hidr&aacute;ulicos.",
        "wa_cta": "Ol&aacute;! Preciso de servi&ccedil;os hidr&aacute;ulicos agora!",
        "img": "servicos-hidraulicos.png",
        "img_alt": "Servi&ccedil;os hidr&aacute;ulicos e reparos",
        "card_title": "Servi&ccedil;os Hidr&aacute;ulicos",
        "card_desc": "Executamos reparos, instala&ccedil;&otilde;es e ajustes hidr&aacute;ulicos com seguran&ccedil;a e qualidade.",
        "tags": ["Residencial", "Comercial", "Condom&iacute;nio", "Vazamentos", "24 horas"],
        "faq_title": "Perguntas frequentes sobre servi&ccedil;os hidr&aacute;ulicos",
        "faqs": [
            ("Faz instala&ccedil;&atilde;o de torneira e chuveiro?", "Sim. Instalamos e ajustamos equipamentos hidr&aacute;ulicos."),
            ("Atende pequenos reparos?", "Sim. Desde pequenos vazamentos at&eacute; servi&ccedil;os completos."),
            ("Tem or&ccedil;amento?", "Sim. Or&ccedil;amento informando o problema antes do servi&ccedil;o."),
            ("Atende condom&iacute;nios?", "Sim. Registros, bombas e &aacute;reas comuns."),
        ],
        "cta_h2": "Precisa de reparo hidr&aacute;ulico?",
        "cta_p": "Solicite or&ccedil;amento para servi&ccedil;os hidr&aacute;ulicos em S&atilde;o Paulo.",
    },
]


def render(svc):
    checklist = "".join(f"<li>{item}</li>" for item in svc["checklist"])
    tags = "".join(f'<span class="tag">{t}</span>' for t in svc["tags"])
    faqs = "".join(
        f'<details class="faq-item"><summary>{q}</summary><div class="faq-answer">{a}</div></details>'
        for q, a in svc["faqs"]
    )

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{svc['title']}</title>
  <meta name="description" content="{svc['meta']}" />
  <meta name="robots" content="index, follow" />
  <meta name="theme-color" content="#0d1b2a" />
  <link rel="canonical" href="https://www.kortesiadesentupidora.com.br/pages/{svc['file']}.html" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../src/css/service-page.css" />
</head>
<body class="service-page">

  <nav class="navbar">
    <a class="navbar-logo" href="../index.html" aria-label="Kortesia Desentupidora">
      <img src="../assets/img/logo.png" alt="Kortesia Desentupidora" width="36" height="36" />
      <span class="navbar-brand">Kortesia</span>
      <span class="navbar-tag">Desentupidora</span>
    </a>
    <nav class="navbar-links" aria-label="Menu principal">
      <a href="../index.html">In&iacute;cio</a>
      <a href="./servicos.html">Servi&ccedil;os</a>
      <a href="./caca-vazamento.html">Ca&ccedil;a Vazamentos</a>
      <a href="../index.html#testimonials">Depoimentos</a>
      <a href="./contato.html">Contato</a>
    </nav>
    <a class="navbar-phone" href="#" data-phone-link>
      {PHONE_SVG}
      <span data-phone-display></span>
    </a>
    <a href="#" class="btn-whatsapp-nav" data-whatsapp-message="Ol&aacute;! Preciso de um or&ccedil;amento." target="_blank" rel="noopener">
      {WA_SVG.replace('width="18"', 'width="16"').replace('height="18"', 'height="16"')}
      WhatsApp
    </a>
  </nav>

  <section class="hero">
    <div>
      <span class="hero-badge">{svc['badge']}</span>
      <h1 class="hero-title">{svc['h1']}<br><span>{svc['h1_span']}</span></h1>
      <p class="hero-desc">{svc['desc']}</p>
      <ul class="hero-checklist">{checklist}</ul>
      <div class="hero-actions">
        <a href="#" class="btn-primary" data-whatsapp-message="{svc['wa']}" target="_blank" rel="noopener">
          {WA_SVG}
          Solicitar or&ccedil;amento
        </a>
        <a href="#" class="btn-secondary" data-phone-link>
          {PHONE_SVG}
          Ligar para emerg&ecirc;ncia
        </a>
      </div>
    </div>
    <div class="hero-card">
      <img class="hero-card-image" src="../assets/img/servicos/{svc['img']}" alt="{svc['img_alt']}" width="800" height="520" />
      <div class="hero-card-body">
        <p class="hero-card-title">{svc['card_title']}</p>
        <p class="hero-card-desc">{svc['card_desc']}</p>
        <div class="hero-card-tags">{tags}</div>
      </div>
    </div>
  </section>

  <div class="banner-emergencia">
    &#9889; Emerg&ecirc;ncia? Atendemos agora!
    <a href="#" data-whatsapp-message="{svc['wa']}" target="_blank" rel="noopener">Solicitar or&ccedil;amento &rarr;</a>
    &nbsp;|&nbsp;
    <a href="#" data-phone-link><span data-phone-display></span></a>
  </div>

  <section class="section">
    <span class="section-label">&#9881; PROCESSO SIMPLES</span>
    <h2 class="section-title">Como funciona o atendimento</h2>
    <p class="section-desc">Do contato &agrave; resolu&ccedil;&atilde;o, nosso processo &eacute; r&aacute;pido e transparente. Voc&ecirc; sabe exatamente o que vai acontecer em cada etapa.</p>
    <div class="steps">
      <div class="step-card"><div class="step-number">1</div><h3>Voc&ecirc; nos chama</h3><p>Pelo WhatsApp ou telefone, em qualquer hor&aacute;rio. Atendemos 24h, incluindo feriados.</p></div>
      <div class="step-card"><div class="step-number">2</div><h3>Envio do t&eacute;cnico</h3><p>Despachamos o t&eacute;cnico mais pr&oacute;ximo imediatamente. Tempo m&eacute;dio de chegada: 30 minutos.</p></div>
      <div class="step-card"><div class="step-number">3</div><h3>Diagn&oacute;stico gratuito</h3><p>O t&eacute;cnico avalia o problema e apresenta or&ccedil;amento antes de iniciar qualquer servi&ccedil;o.</p></div>
      <div class="step-card"><div class="step-number">4</div><h3>Servi&ccedil;o realizado</h3><p>Problema resolvido com equipamento adequado. Local limpo ao final do atendimento.</p></div>
    </div>
  </section>

  <section class="section-dark">
    <span class="section-label">&#9733; POR QUE A KORTESIA</span>
    <h2 class="section-title">Por que escolher a Kortesia?</h2>
    <p class="section-desc">Mais de 5.000 atendimentos realizados em S&atilde;o Paulo com avalia&ccedil;&atilde;o 4,8 no Google.</p>
    <div class="diferenciais">
      <div class="diferencial-card"><div class="diferencial-icon"><svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg></div><h3>Atendimento 24h</h3><p>Dispon&iacute;veis todos os dias, incluindo finais de semana e feriados.</p></div>
      <div class="diferencial-card"><div class="diferencial-icon"><svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div><h3>Equipe identificada</h3><p>T&eacute;cnicos uniformizados, com crach&aacute; e ve&iacute;culo identificado.</p></div>
      <div class="diferencial-card"><div class="diferencial-icon"><svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"/></svg></div><h3>Or&ccedil;amento transparente</h3><p>Voc&ecirc; aprova o valor antes de iniciarmos. Sem cobran&ccedil;as surpresa.</p></div>
      <div class="diferencial-card"><div class="diferencial-icon"><svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg></div><h3>Garantia do servi&ccedil;o</h3><p>Garantimos o resultado. Se o problema voltar, retornamos sem custo adicional.</p></div>
    </div>
    <div class="stats">
      <div class="stat-box"><div class="val">+5k</div><div class="lbl">Atendimentos realizados</div></div>
      <div class="stat-box"><div class="val">&#9733; 4,8</div><div class="lbl">Avalia&ccedil;&atilde;o no Google</div></div>
      <div class="stat-box"><div class="val">30min</div><div class="lbl">Tempo de resposta</div></div>
      <div class="stat-box"><div class="val">24h</div><div class="lbl">Disponibilidade</div></div>
    </div>
  </section>

  <section class="section">
    <span class="section-label">? D&Uacute;VIDAS FREQUENTES</span>
    <h2 class="section-title">{svc['faq_title']}</h2>
    <p class="section-desc">Respondemos as d&uacute;vidas mais comuns dos nossos clientes.</p>
    <div class="faq-list">{faqs}</div>
  </section>

  <section class="cta-section">
    <h2>{svc['cta_h2']}</h2>
    <p>{svc['cta_p']}</p>
    <div class="cta-buttons">
      <a href="#" class="btn-primary" data-whatsapp-message="{svc['wa_cta']}" target="_blank" rel="noopener">
        {WA_SVG}
        Solicitar or&ccedil;amento
      </a>
      <a href="#" class="btn-secondary" data-phone-link>
        {PHONE_SVG}
        <span data-phone-display></span>
      </a>
    </div>
  </section>

  <footer class="service-footer">
    <span>&copy; 2026 Kortesia Desentupidora &middot; S&atilde;o Paulo, SP</span>
    <span><a href="../index.html">Voltar ao in&iacute;cio</a> &middot; <a href="./servicos.html">Todos os servi&ccedil;os</a></span>
  </footer>

  <a href="#" class="fab-whatsapp" data-whatsapp-message="{svc['wa']}" target="_blank" rel="noopener" aria-label="Solicitar or&ccedil;amento no WhatsApp">
    {WA_SVG.replace('width="18"', 'width="28"').replace('height="18"', 'height="28"')}
  </a>

  <script defer src="../src/js/config.js"></script>
  <script defer src="../src/js/whatsapp.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', function () {{
      if (window.KortesiaWhatsApp) window.KortesiaWhatsApp.applyContactLinks();
    }});
  </script>
</body>
</html>
"""


if __name__ == "__main__":
    PAGES.mkdir(parents=True, exist_ok=True)
    for svc in SERVICES:
        path = PAGES / f"{svc['file']}.html"
        path.write_text(render(svc), encoding="utf-8")
        print("Created", path.name)
