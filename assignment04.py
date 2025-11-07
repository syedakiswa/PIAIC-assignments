from flask import Flask, render_template, request, jsonify
from textblob import TextBlob
import random

app = Flask(__name__)

quotes = {
    'happy': [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "The best way to predict the future is to create it. - Abraham Lincoln",
        "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill"
    ],
    'sad': [
        "The only way out of the labyrinth of suffering is to forgive. - John Green",
        "Tears come from the heart and not from the brain. - Leonardo da Vinci",
        "The word 'happy' would lose its meaning if it were not balanced by sadness. - Carl Jung"
    ],
    'angry': [
        "For every minute you remain angry, you give up sixty seconds of peace of mind. - Ralph Waldo Emerson",
        "Anger is an acid that can do more harm to the vessel in which it is stored than to anything on which it is poured. - Mark Twain",
        "The greatest remedy for anger is delay. - Seneca"
    ],
    'neutral': [
        "The present moment is filled with joy and happiness. If you are attentive, you will see it. - Thich Nhat Hanh",
        "The future depends on what you do today. - Mahatma Gandhi",
        "Life is 10% what happens to us and 90% how we react to it. - Charles R. Swindoll"
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check-mood', methods=['POST'])
def check_mood():
    text = request.json['text']
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.5:
        mood = 'happy'
        emoji = '😄'
        message = 'You seem happy!'
        color = '#FFD700'  # Gold
    elif polarity < -0.5:
        mood = 'angry'
        emoji = '😠'
        message = 'You seem angry.'
        color = '#FF6347'  # Tomato
    elif polarity < 0:
        mood = 'sad'
        emoji = '😢'
        message = 'You seem sad.'
        color = '#ADD8E6'  # Light Blue
    else:
        mood = 'neutral'
        emoji = '😐'
        message = 'You seem neutral.'
        color = '#FFFFFF'  # White

    quote = random.choice(quotes[mood])

    return jsonify({
        'emoji': emoji,
        'message': message,
        'quote': quote,
        'color': color
    })

if __name__ == '__main__':
    app.run(debug=True)
