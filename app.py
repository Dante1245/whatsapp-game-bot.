from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/webhook", methods=['POST'])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').strip()
    resp = MessagingResponse()
    msg = resp.message()

    # Example response
    if incoming_msg.lower() == 'hi':
        msg.body("Hello! Pick a number from 1 to 110.")
    else:
        msg.body("Thanks! Let's continue the game.")

    return str(resp)
