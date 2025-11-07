import random

def registration():
    """Registers a new user."""
    print("--- Registration ---")
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    return username, password

def login(registered_username, registered_password):
    """Logs in a user."""
    print("--- Login ---")
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username == registered_username and password == registered_password:
            print("Login successful!")
            return True
        else:
            print("Invalid username or password. Please try again.")

def select_difficulty():
    """Allows the user to select a difficulty level."""
    print("--- Select Difficulty ---")
    print("1. Easy (Unlimited tries)")
    print("2. Medium (5 tries)")
    print("3. Hard (3 tries)")
    while True:
        choice = input("Choose a difficulty (1-3): ")
        if choice == '1':
            return "easy"
        elif choice == '2':
            return "medium"
        elif choice == '3':
            return "hard"
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def play_game(difficulty):
    """The main game loop."""
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = {
        "easy": float('inf'),
        "medium": 5,
        "hard": 3
    }[difficulty]

    print(f"\nI'm thinking of a number between 1 and 100. You have {max_attempts if max_attempts != float('inf') else 'unlimited'} tries.")

    while attempts < max_attempts:
        try:
            guess = int(input("Your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                score = ((max_attempts - (attempts -1)) / max_attempts) * 100 if max_attempts != float('inf') else 100
                print(f"Congratulations! You guessed the number in {attempts} tries.")
                print(f"Your score: {score:.2f}%")
                review = input("Please give a short review of the game: ")
                return True
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"\nSorry, you ran out of tries. The number was {secret_number}.")
    return False

def main():
    """Main function to run the game."""
    registered_username, registered_password = registration()
    if login(registered_username, registered_password):
        while True:
            difficulty = select_difficulty()
            if play_game(difficulty):
                play_again = input("Do you want to play again? (yes/no): ")
                if play_again.lower() != 'yes':
                    break
            else:
                try_again = input("Try again? (yes/no): ")
                if try_again.lower() != 'yes':
                    break

if __name__ == "__main__":
    main()
