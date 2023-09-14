import random

# Read the list of words from a file
with open('Python.txt', 'r') as f:
    words = [word.strip() for word in f]

# Select a random word from the list
word = random.choice(words)

# Track the guessed letters and the number of incorrect guesses
guessed_letters = set()
incorrect_guesses = 0

# Hangman graphic
hangman = [
    '----\n|   |\n|\n|\n|\n|\n',
    '----\n|   |\n|   O\n|\n|\n|\n',
    '----\n|   |\n|   O\n|   |\n|\n|\n',
    '----\n|   |\n|   O\n|  /|\n|\n|\n',
    '----\n|   |\n|   O\n|  /|\\\n|\n|\n',
    '----\n|   |\n|   O\n|  /|\\\n|  /\n|\n',
    '----\n|   |\n|   O\n|  /|\\\n|  / \\\n|\n',
]

# Loop until the word is guessed or the player runs out of guesses
while True:
    # Display the current state of the word
    display_word = ''
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += '_'
    print('Word:', display_word)

    # Check if the word has been guessed
    if '_' not in display_word:
        print('Congratulations, you guessed the word!')
        break

    # Ask the player to guess a letter
    guess = input('Guess a letter: ').lower()

    # Check if the letter has already been guessed
    if guess in guessed_letters:
        print('You already guessed that letter.')
        continue

    # Add the letter to the guessed letters set
    guessed_letters.add(guess)

    # Check if the letter is in the word
    if guess in word:
        print('Correct!')
    else:
        print('Incorrect.')
        incorrect_guesses += 1

        # Display hangman graphic
        print(hangman[incorrect_guesses - 1])

        # Check if the player has used up all their guesses
        if incorrect_guesses == 6:
            print('Sorry, you ran out of guesses. The word was', word)
            break
