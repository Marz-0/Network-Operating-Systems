import random

def hangman():
    word_list = ["python", "java", "javascript"]  # List of words to choose from
    chosen_word = random.choice(word_list)  # Randomly selecting a word
    guessed_letters = set()
    max_guesses = 6
    incorrect_guesses = 0
    display_word = ['_' for _ in chosen_word]  # Creating blanks for the word
    
    print("Welcome to Hangman!")
    
    while incorrect_guesses < max_guesses and '_' in display_word:
        print(" ".join(display_word))  # Display the word with guessed letters
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        guessed_letters.add(guess)
        
        if guess in chosen_word:
            # Reveal correctly guessed letters
            for i, letter in enumerate(chosen_word):
                if letter == guess:
                    display_word[i] = guess
        else:
            incorrect_guesses += 1
            print(f"Incorrect! You have {max_guesses - incorrect_guesses} guesses left.")
    
    if '_' not in display_word:
        print(f"Congratulations, you guessed the word '{chosen_word}'!")
    else:
        print(f"Game over! The word was '{chosen_word}'.")

if __name__ == "__main__":
    hangman()
