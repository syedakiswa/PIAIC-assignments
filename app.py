
from flask import Flask, render_template

app = Flask(__name__)

# Placeholder data
matches = [
    {
        "title": "Pakistan vs South Africa 2025",
        "score": "PAK: 250/5 (50) | SA: 251/4 (48.2)",
        "status": "South Africa won by 6 wickets"
    },
    {
        "title": "Australia vs England 2025",
        "score": "AUS: 300/7 (50) | ENG: 150/10 (35.2)",
        "status": "Australia won by 150 runs"
    }
]

@app.route('/')
def index():
    return render_template('index.html', matches=matches)

if __name__ == '__main__':
    app.run(debug=True)
