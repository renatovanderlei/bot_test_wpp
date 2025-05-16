import os
from flask import Flask, request, url_for
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/bot", methods=["POST"])
def bot():
    incoming = request.form.get('Body', '').strip().lower()
    resp = MessagingResponse()
    msg = resp.message()

    if 'interesse' in incoming:
        # URL base do seu deploy: Render define isso como HOST_DYNAMIC
        base = request.url_root.rstrip('/')  
        img_url = f"{base}{url_for('static', filename='congresso.png')}"
        pdf_url = f"{base}{url_for('static', filename='programa.pdf')}"

        texto = (
            "Olá, Seja Bem-Vindo(a)!\n"
            "Sou da equipe de Consultores Comerciais da WAP Cursos. Recebemos sua mensagem e ficamos felizes pelo seu interesse no 3° Congresso de Contratações Públicas do Nordeste.\n\n"
            "Detalhes do Evento\n"
            "📍- Local: Centro de Convenções de Maceió\n"
            "🗓- Datas: 29, 30 e 31 de julho de 2025\n\n"
            "Vantagens\n"
            "- Palestrantes renomados\n"
            "- Network impactante\n"
            "- Atualização em contratações públicas\n"
            "- Coffee break\n"
            "- Kit com material\n\n"
            "💰 Investimento:\n"
            "- 2° Lote: R$ 1.897,00\n"
            "- 3° Lote: R$ 2.597,00\n\n"
            "Contato\n"
            "Para mais informações, por favor, forneça os seguintes dados:\n\n"
            "- Nome\n"
            "- Órgão ou Pessoa Física\n"
            "- E-mail\n"
            "- Quantidade de pessoas\n"
            "- Contato\n"
            "- Adiantaremos orçamento/proposta.\n"
            "Segue programação do evento.\n\n"
            "📞Contato Comercial\n"
            "- (82) 99967-8041 / 98830-6001\n"
            "- (92) 99988-9069 - Blenda Libório | Consultora Comercial\n\n"
            "Estamos à disposição para esclarecer suas dúvidas."
        )

        msg.body(texto)
        msg.media(img_url)
        msg.media(pdf_url)

    else:
        msg.body("Desculpe, não entendi. Digite algo contendo 'interesse' para receber informações.")

    return str(resp)


if __name__ == "__main__":
    # Porta que o Render expõe ao container
    port = int(os.environ.get("PORT", 5000))
    # Escuta em 0.0.0.0 pra ficar acessível externamente
    app.run(host="0.0.0.0", port=port)
