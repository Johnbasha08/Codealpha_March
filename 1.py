
import random

def choose_word():
    words = ["hangman", "python", "linkedin", "coding", "challenge", "programming"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Guess the word:", display_word(word, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
            print(display_word(word, guessed_letters))
        else:
            attempts -= 1
            print("Incorrect! You have", attempts, "attempts left.")
            print(display_word(word, guessed_letters))

        if "_" not in display_word(word, guessed_letters):
            print("Congratulations! You guessed the word:", word)
            break

    if attempts == 0:
        print("Sorry, you're out of attempts. The word was:", word)

if __name__ == "__main__":
    hangman()
