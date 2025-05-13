from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# List of questions
questions = [
    "What age did you have your first sex?",
    "Do you or have you smoked?",
    "Ever had sex with someone you don't love?",
    "Wanna kiss me?",
    "Ever kissed someone of the same gender?",
    "Send me 2 pics of your pussy.",
    "What's your best color?",
    "What's your favorite sex position?",
    "Ever been abused?",
    "Tell me how you had your last sex, in detail.",
    "Do you watch porn?",
    "How long do you want sex to last?",
    "Do you love me?",
    "Are you naughty?",
    "Favorite body part of your opposite gender?",
    "Ever had sex?",
    "Would you kiss me?",
    "Do you drink alcohol?",
    "Ever begged for sex?",
    "Do you want to fuck me?",
    "Have you ever played someone?",
    "What turns you on?",
    "Ever had sex with a same gender person?",
    "Tell me 3 of your deepest secrets.",
    "Best friend?",
    "Do you love sex?",
    "Use my pic as your DP for 1 week.",
    "Wanna date me?",
    "What year did you have your first sex?",
    "Favorite clothes?",
    "Ever made out?",
    "Best hobby?",
    "Have you ever masturbated?",
    "Your crush?",
    "Complete d**k.",
    "Complete p***y.",
    "Do you go to night parties?",
    "Do you want to explore me?",
    "Send me your dance videos.",
    "Do you like BJ?",
    "Have you ever been played?",
    "If you see me naked, what would you do?",
    "Buy me a gift.",
    "Will you let me finger you or stroke your dick?",
    "Send me 2 pics of your dick.",
    "Promise to have sex with me.",
    "Do you sex chat?",
    "Ever exchanged nude?",
    "Tell me things you want from me.",
    "Do you love me?",
    "Are you a virgin?",
    "Have some mistakenly seen your dick or pussy?",
    "How much do you enjoy sex?",
    "Would you let me touch you?",
    "Tell me how you really feel about me.",
    "Player or loyal?",
    "Would you have sex with me?"
]
random.shuffle(questions)

answered = []
unanswered = list(questions)

@app.route('/')
def home():
    return "Pick-a-Number WhatsApp Bot is running!"

@app.route('/webhook', methods=['POST'])
def whatsapp_webhook():
    incoming_msg = request.values.get('Body', '').strip().lower()
    sender = request.values.get('From', '')

    if incoming_msg.isdigit():
        num = int(incoming_msg)
        if 1 <= num <= len(questions):
            question = questions[num - 1]
            if question not in answered:
                answered.append(question)
                unanswered.remove(question)
                reply = f"{question}\n\nAnswered: {len(answered)} | Left: {len(unanswered)}"
            else:
                reply = f"Question {num} already answered. Try another!"
        else:
            reply = f"Pick a number between 1 and {len(questions)}."
    else:
        reply = f"Welcome to the Pick-a-Number game! Reply with a number (1-{len(questions)})."

    return jsonify({"message": reply})

if __name__ == '__main__':
    app.run()
