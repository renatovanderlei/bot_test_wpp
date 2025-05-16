from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/bot", methods=['POST'])
def bot():
    incoming_msg = request.form.get('Body')
    resp = MessagingResponse()

    if incoming_msg.strip().lower() == 'oi':
        resp.message("Oi! Tudo bem? Eu sou o RenatoBot 🤖")
    else:
        resp.message("Desculpa, não entendi. Envie 'oi' para começar.")

    return str(resp)

if __name__ == "__main__":
    app.run()
