from flask import Flask, request, Response
from twilio.twiml.messaging_response import MessagingResponse
import random

app = Flask(__name__)

# Complete list of 110 questions
questions = {
    1: "What age did you have your first sex?",
    2: "Do you or have you smoked?",
    3: "Ever had sex with someone you don't love?",
    4: "Wanna kiss me?",
    5: "Ever kissed someone of the same gender?",
    6: "Send me 2 pics of your pussy.",
    7: "What's your best color?",
    8: "What's your favorite sex position?",
    9: "Ever been abused?",
    10: "Tell me how you had your last sex, in detail.",
    11: "Do you watch porn?",
    12: "How long do you want sex to last?",
    13: "Do you love me?",
    14: "Are you naughty?",
    15: "Favorite body part of your opposite gender?",
    16: "Ever had sex?",
    17: "Would you kiss me?",
    18: "Do you drink alcohol?",
    19: "Ever begged for sex?",
    20: "Do you want to fuck me?",
    21: "Have you ever played someone?",
    22: "What turns you on?",
    23: "Ever had sex with a same gender person?",
    24: "Tell me 3 of your deepest secrets.",
    25: "Best friend?",
    26: "Do you love sex?",
    27: "Use my pic as your DP for 1 week.",
    28: "Wanna date me?",
    29: "What year did you have your first sex?",
    30: "Favorite clothes?",
    31: "Ever made out?",
    32: "Best hobby?",
    33: "Have you ever masturbated?",
    34: "Your crush?",
    35: "Complete d**k.",
    36: "Complete p***y.",
    37: "Do you go to night parties?",
    38: "Do you want to explore me?",
    39: "Send me your dance videos.",
    40: "Do you like BJ?",
    41: "Have you ever been played?",
    42: "If you see me naked, what would you do?",
    43: "Buy me a gift.",
    44: "Will you let me finger you or stroke your dick?",
    45: "Send me 2 pics of your dick.",
    46: "Promise to have sex with me.",
    47: "Do you sex chat?",
    48: "Ever exchanged nude?",
    49: "Tell me things you want from me.",
    50: "Do you love me?",
    51: "Are you a virgin?",
    52: "Have some mistakenly seen your dick or pussy?",
    53: "How much do you enjoy sex?",
    54: "Would you let me touch you?",
    55: "Tell me how you really feel about me.",
    56: "Player or loyal?",
    57: "Would you have sex with me?",
    58: "What do you love doing the most?",
    59: "Birthday?",
    60: "Ever fucked someone hard and cried?",
    61: "Ever slept naked?",
    62: "What's your biggest fear?",
    63: "Single or taken?",
    64: "Favorite song?",
    65: "Favorite movie?",
    66: "Nickname?",
    67: "Would you kiss me when we meet?",
    68: "Would you watch porn with me or give me a BJ?",
    69: "Hairy dick/pussy or shaved?",
    70: "Do you always wear a bra?",
    71: "Do you always wear panties?",
    72: "Promise to kiss me when we meet.",
    73: "If you have the chance, would you date me?",
    74: "Wanna fuck me?",
    75: "Tell me an erotic story.",
    76: "Shy or bold?",
    77: "Ever been so horny you begged for it?",
    78: "Tell me a naughty story.",
    79: "How do you want the dick or pussy to be?",
    80: "Big dicks or normal dicks?",
    81: "Big pussy or normal pussy?",
    82: "Do you prefer a hard fuck or a soft one?",
    83: "Will you kiss me when we meet?",
    84: "Send me your breast or chest picture.",
    85: "Send me your nude pics or porn videos.",
    86: "Would you kiss me right now if I asked?",
    87: "What gets you wet?",
    88: "Do you prefer licking or sucking?",
    89: "Do you wear bras all the time?",
    90: "Do you want to have sex with me?",
    91: "Favorite body part on yourself?",
    92: "What's your happiest moment?",
    93: "What's your worst mistake?",
    94: "Describe your most enjoyable sex in detail.",
    95: "Favorite time to have sex?",
    96: "Best memory?",
    97: "Send me your twerking video.",
    98: "Ever had sex and cried from pleasure?",
    99: "Favorite sex outfit?",
    100: "Do you moan during sex?",
    101: "Do you want to sex chat with me right now?",
    102: "Tell me one naughty thing you'd like me to do to you.",
    103: "Last time you cried and why?",
    104: "Ask me anything.",
    105: "Do you want to try something kinky with me?",
    106: "Tell me one thing you'd change about yourself.",
    107: "Last kiss and with who?",
    108: "Last sex?",
    109: "Would you give me a kiss or a hug?",
    110: "Send me two of your sexiest pics."
}

answered_questions = set()

@app.route('/webhook', methods=['POST'])
def webhook():
    incoming_msg = request.values.get('Body', '').strip()
    resp = MessagingResponse()

    if incoming_msg.lower() in ['start', 'play']:
        remaining = [num for num in questions if num not in answered_questions]
        if not remaining:
            resp.message("You’ve answered all questions!")
        else:
            choice = random.choice(remaining)
            answered_questions.add(choice)
            resp.message(f"Question {choice}: {questions[choice]}")
    elif incoming_msg.isdigit():
        num = int(incoming_msg)
        if num in questions:
            if num in answered_questions:
                resp.message(f"Question {num} has already been answered.")
            else:
                answered_questions.add(num)
                resp.message(f"Question {num}: {questions[num]}")
        else:
            resp.message("Invalid number. Choose between 1 and 110.")
    else:
        resp.message("Type 'start' or choose a number (1-110) to play.")

    return Response(str(resp), mimetype="application/xml")

@app.route('/status', methods=['POST'])
def status():
    sid = request.form.get('MessageSid')
    status = request.form.get('MessageStatus')
    print(f"Message SID {sid} changed status to {status}")
    return ('', 200)

if __name__ == "__main__":
    app.run()