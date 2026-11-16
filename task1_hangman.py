import random

WORDS = ["python", "laptop", "keyboard", "program", "internet","function", "variable", "network", "monitor", "database","developer", "software", "compiler", "package", "library"]
MAX_WRONG = 6


def play(word):
    guessed = []
    wrong = 0

    while wrong < MAX_WRONG:
        shown = " ".join(ch if ch in guessed else "_" for ch in word)
        print("\nWord:", shown)
        print("Wrong guesses left:", MAX_WRONG - wrong)

        if "_" not in shown:
            print("You got it! The word was", word)
            return

        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Type a single letter.")
        elif guess in guessed:
            print("You already tried that one.")
        else:
            guessed.append(guess)
            if guess in word:
                print("Good guess.")
            else:
                wrong += 1
                print("Nope, that letter isn't in the word.")

    print("\nGame over. The word was", word)


def main():
    last = ""
    while True:
        choices = [w for w in WORDS if w != last]
        word = random.choice(choices)
        last = word

        play(word)

        again = input("\nPlay again? (y/n): ").lower().strip()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()