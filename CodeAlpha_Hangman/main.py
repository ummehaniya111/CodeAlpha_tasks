import random

# List of words for the game
word_list = ["python", "website", "developer", "coding", "technology", "function", "variable"]

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

def hangman():
    word = random.choice(word_list)
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!")

    while attempts > 0:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Guessed letters: {' '.join(guessed_letters)}")
        print(f"Remaining attempts: {attempts}")

        guess = input("Enter the letter : ").lower() 

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Good guess!")
        else:
            guessed_letters.add(guess)
            attempts -= 1
            print("Wrong guess!")

        display = display_word(word,guessed_letters)
        if "_" not in display:
            print(f"Word : {display}")
            print(f"\nCongratulations! You guessed the word: {word}")
            break
    else:
        print(f"\nSorry, you ran out of attempts. The word was: {word}")

if __name__ == "__main__":
    hangman()
