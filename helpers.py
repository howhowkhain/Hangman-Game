import time
import random


def main():
    words_list = ['mama', 'masina', 'casa', 'mamaliga', 'iubire']
    word = random.choice(words_list)
    word_length = len(word)
    print(f'Your word have: {word_length} letters')
    word_line = '_ ' * word_length
    print(word_line)
    count = 0
    count_limit = 8
    correct_guesses = 0
    guessed_word = word_line.split()
    print(guessed_word)
    print(f'You have: {count_limit + 1} tries. Good luck!\n')
    draw(count_limit)
    wrong_letters = []
    while count < (count_limit + 1):
        guess_letter = input('Guess the letter: ').lower()
        if len(guess_letter) == 1:
            if guess_letter in word:
                for index in range(word_length):
                    if word[index] == guess_letter:
                        guessed_word[index] = guess_letter
                correct_guesses += 1
                print(
                    f'You guest this letters: {guessed_word}',
                    f'\nRemaining letters: {guessed_word.count("_")}',
                    f'Remaining tries: {count_limit - (len(wrong_letters) + correct_guesses) + 1}\n'
                )
                if '_' not in guessed_word:
                    print('Game over. You win!')
                    loop()
                count += 1
            else:
                wrong_letters.append(guess_letter)
                wrong_letters_length = len(wrong_letters)
                print(
                    f'Wrong letter: {wrong_letters}; {len(wrong_letters)}',
                    f'Remaining tries: {count_limit - (len(wrong_letters) + correct_guesses) + 1}'
                )
                image(wrong_letters_length)
                if count != count_limit:
                    print('Try again!\n')
                count += 1
        else:
            print('Wrong input. Try again, please!')
            count == count
    else:
        print('Game over. You lost!')
        image(9)
        print(word)
        loop()


def draw(count_limit):
    print("  _________ ")
    for i in range(count_limit):
        print("  | ")
    print("__|__")


def image(wrong_letters_length):
    if wrong_letters_length == 1:
        time.sleep(1)
        print("  _________  \n"
              "  |        | \n"
              "  |          \n"
              "  |          \n"
              "  |          \n"
              "  |          \n"
              "  |          \n"
              "  |          \n"
              "__|__        \n"
              )
    elif wrong_letters_length == 2:
        time.sleep(1)
        print("  _________  \n"
              "  |        | \n"
              "  |        | \n"
              "  |          \n"
              "  |          \n"
              "  |          \n"
              "  |          \n"
              "  |          \n"
              "__|__        \n"
              )
    elif wrong_letters_length == 3:
        time.sleep(1)
        print("  _________  \n"
              "  |        | \n"
              "  |        | \n"
              "  |        0 \n"
              "  |          \n"
              "  |          \n"
              "  |          \n"
              "  |          \n"
              "__|__        \n"
              )
    elif wrong_letters_length == 4:
        time.sleep(1)
        print("  _________  \n"
              "  |        | \n"
              "  |        | \n"
              "  |        0 \n"
              "  |        | \n"
              "  |          \n"
              "  |          \n"
              "  |          \n"
              "__|__        \n"
              )
    elif wrong_letters_length == 5:
        time.sleep(1)
        print("  _________  \n"
              "  |        | \n"
              "  |        | \n"
              "  |        0 \n"
              "  |        | \n"
              "  |        | \n"
              "  |          \n"
              "  |          \n"
              "__|__        \n"
              )
    elif wrong_letters_length == 6:
        time.sleep(1)
        print("  _________  \n"
              "  |        | \n"
              "  |        | \n"
              "  |        0 \n"
              "  |       /| \n"
              "  |        | \n"
              "  |          \n"
              "  |          \n"
              "__|__        \n"
              )
    elif wrong_letters_length == 7:
        time.sleep(1)
        print("  _________   \n"
              "  |        |  \n"
              "  |        |  \n"
              "  |        0  \n"
              "  |       /|\ \n"
              "  |        |  \n"
              "  |           \n"
              "  |           \n"
              "__|__         \n"
              )
    elif wrong_letters_length == 8:
        time.sleep(1)
        print("  _________   \n"
              "  |        |  \n"
              "  |        |  \n"
              "  |        0  \n"
              "  |       /|\ \n"
              "  |        |  \n"
              "  |       /   \n"
              "  |           \n"
              "__|__         \n"
              )
    elif wrong_letters_length == 9:
        time.sleep(1)
        print("  _________   \n"
              "  |        |  \n"
              "  |        |  \n"
              "  |        0  \n"
              "  |       /|\ \n"
              "  |        |  \n"
              "  |       / \ \n"
              "  |           \n"
              "__|__         \n"
              )


def loop():
    print('Do you want to play again?')
    option = input('Choose: y = yes or n = no ').lower()
    if option == 'y':
        main()
    elif option == 'n':
        print('Thank you for playing. We expect you back again!')
        exit()
    else:
        print('Wrong input! Choose: y = yes or n = no')
