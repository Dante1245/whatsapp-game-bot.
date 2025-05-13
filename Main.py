from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import random

app = Flask(__name__)

# Load all 110 questions
questions = [
    "1. Birthday", "2. Worst mistake", "3. Ur greatest fear", "4. Crush", "5. Best colour",
    "6. Do u or have u smoked?", "7. Do u drink alcohol?", "8. Do u go for nyt parties?",
    "9. Last time u cried and wat caused it", "10. Ur dreams", "11. Have u or do u maturate?",
    "12. Happiest moment", "13. Best memory", "14. Last kiss and wit who", "15. Do you watch porn?",
    "16. Your best body part", "17. Ever been fucked hard nd u cried?", "18. Complete d**k",
    "19. Complete p***y", "20. Ur most enjoyable sex,tel me abt it in details", "21. Full name",
    "22. If u have d chance wil u date me?", "23. Will u kiss me?", "24. Kiss or hug",
    "25. Favorite song", "26. Favorite movie", "27. Ever kissed a same gender person?",
    "28. Do u love bj?", "29. Send me ur number", "30. Ever maked out?", "31. Wanna explore me?",
    "32. Wanna kiss me?", "33. Wanna fuck me?", "34. Wanna date me?", "35. Ever been abused?",
    "36. Best hubby", "37. Tel me 3 deepest secrets", "38. Send me ur nude pics or porn videos",
    "39. Favorite body part of ur opposite gender", "40. Big dicks or normal dicks",
    "41. Big pussy or normal pussy", "42. Promise to kiss me wen we meet",
    "43. Tell me how u really feel about me", "44. Tell me a story", "45. Do u wear bra?",
    "46. Do u always wear pant?", "47. Promise to watch porn wit me or gv me a Bj",
    "48. Will u let me finger u or stroke ur dick?", "49. Wat age did u have ur first sex",
    "50. Wat year did u have ur first sex", "51. Player or loyal", "52. Single or taken",
    "53. Have you ever been played?", "54. Have you ever played someone?",
    "55. Tell me an erotic story", "56. Last sex", "57. Ever had sex wit a same gender person?",
    "58. Use my pic as ur dp for 1 week", "59. Send me ur breast or chest picture",
    "60. Do u sex chat?", "61. If u see me naked, wat will u do", "62. Shy or bold",
    "63. Ever slept naked?", "64. Virgin?", "65. Wat turns u on", "66. What do you love doing the most",
    "67. Ever begged for sex?", "68. D craziest tin u have ever done", "69. Best friend",
    "70. Ever had sex?", "71. Age", "72. Are you naughty?", "73. Naughtiest tin u have ever done",
    "74. Ever exchanged nude?", "75. Buy me a gift", "76. Wil you let me touch you?",
    "77. Do you love me?", "78. How do you want d dick or pussy to be.", "79. Sex chat with me",
    "80. Have some mistakenly seeing ur dick or pussy?", "81. What gets u wet",
    "82. Last time u felt like having sex", "83. Favorite clothes", "84. Ask me anything",
    "85. Promise to have sex with me", "86. Nickname", "87. Favorite sex position",
    "88. How long do you want sex to be.", "89. Do you love sex?", "90. Something u will change about yourself",
    "91. Send me two of your sexiest pics", "92. Tell me how you had ur last time sex in details",
    "93. How much do you enjoy sex", "94. Tell me things you want from me.", "95. Hard fuck or normal",
    "96. Send me 2 pics of your dick", "97. Send me 2 pics of your pussy", "98. Hairy dick/pussy or shaved",
    "99. Send me your dance videos", "100. Will you fuck me?", "101. Ever fucked someone you don't love?",
    "102. Send me your twerking video", "103. What’s your wildest fantasy?",
    "104. Would you try public sex?", "105. Send me a kiss emoji", "106. Moan for me in voice note",
    "107. Favorite romantic song", "108. Do you prefer fast or slow sex?", "109. Describe a perfect night with me",
    "110. How would you seduce me?"
]

# Shuffle once and keep order
shuffled = random.sample(range(1, 111), 110)
answered = set()

@app.route("/webhook", methods=["POST"])
def whatsapp_bot():
    incoming_msg = request.values.get('Body', '').strip()
    resp = MessagingResponse()
    msg = resp.message()

    if incoming_msg.lower() in ['hi', 'start', 'play']:
        remaining = [num for num in shuffled if num not in answered]
        if not remaining:
            msg.body("Game over! All 110 questions have been answered.")
        else:
            msg.body("Welcome to the *Pick-a-Number* game!\nChoose a number between 1 and 110.")
        return str(resp)

    if incoming_msg.isdigit():
        num = int(incoming_msg)
        if num < 1 or num > 110:
            msg.body("Please pick a number between 1 and 110.")
        elif num in answered:
            msg.body(f"Number {num} has already been picked. Try another.")
        else:
            question = questions[num - 1]
            answered.add(num)
            msg.body(f"Question {num}: {question}\n\n(Answered: {len(answered)}, Remaining: {110 - len(answered)})")
    else:
        msg.body("Send a number (1-110) to get your question. Or type 'start' to begin.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)