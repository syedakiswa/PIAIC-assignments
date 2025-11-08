
import random
from textblob import TextBlob
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

def get_mood(text):
    """
    Analyzes the text and returns the mood (happy, sad, angry, neutral)
    and the polarity score.
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.5:
        return "happy", polarity
    elif polarity > 0.0:
        return "neutral", polarity
    elif polarity < -0.5:
        return "angry", polarity
    else:
        return "sad", polarity

def get_random_quote(mood):
    """
    Returns a random motivational quote based on the mood.
    """
    quotes = {
        "happy": [
            "The best way to predict the future is to create it.",
            "The only way to do great work is to love what you do.",
            "Success is not final, failure is not fatal: it is the courage to continue that counts.",
        ],
        "sad": [
            "The only way out of the labyrinth of suffering is to forgive.",
            "The wound is the place where the Light enters you.",
            "Tough times never last, but tough people do.",
        ],
        "angry": [
            "For every minute you remain angry, you give up sixty seconds of peace of mind.",
            "The greatest remedy for anger is delay.",
            "Holding on to anger is like grasping a hot coal with the intent of throwing it at someone else; you are the one who gets burned.",
        ],
        "neutral": [
            "The present moment is filled with joy and happiness. If you are attentive, you will see it.",
            "The little things? The little moments? They aren't little.",
            "Life is a journey that must be traveled no matter how bad the roads and accommodations.",
        ],
    }
    return random.choice(quotes[mood])

def main():
    """
    Main function to run the mood checker CLI app.
    """
    print(Fore.CYAN + "Welcome to the Mood Checker!")
    print(Fore.CYAN + "Type something and I'll tell you your mood.")
    print(Fore.CYAN + "Type 'exit' to quit.")

    while True:
        user_input = input("> ")
        if user_input.lower() == "exit":
            break

        mood, polarity = get_mood(user_input)
        quote = get_random_quote(mood)

        if mood == "happy":
            emoji = "😊"
            color = Fore.YELLOW
            mood_text = "You seem happy!"
        elif mood == "sad":
            emoji = "😢"
            color = Fore.BLUE
            mood_text = "You seem sad."
        elif mood == "angry":
            emoji = "😠"
            color = Fore.RED
            mood_text = "You seem angry."
        else:
            emoji = "😐"
            color = Fore.WHITE
            mood_text = "You seem neutral."

        print(color + f"{mood_text} {emoji}")
        print(color + f'"{quote}"')

if __name__ == "__main__":
    main()
