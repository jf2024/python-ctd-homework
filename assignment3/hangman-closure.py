# task 4

def make_hangman(secret_word):
    guesses = set()

    def hangman_closure(letter):
        if letter in guesses:
            print("Already guessed that letter! Pick a different one")

        guesses.add(letter)
        print(guesses)

        display = []
        for l in secret_word:
            if l in guesses:
                display.append(l)
            else:
                display.append("_")

        print("".join(display))

        return False if "_" in display else True

    return hangman_closure

word = input("Give a secret word: " )
game = make_hangman(word)

done = False
while not done:
    guess = input("Give a letter please: ")
    done = game(guess)

