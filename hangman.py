import random
from nltk.corpus import words


def choose_difficulty_level():
    level = input("Choose a difficulty level(easy/medium/hard: ").lower()
    if level == "easy":
        return 7
    elif level == "medium":
        return 5
    elif level == "hard":
        return 3
    else:
        print("Wrong choice")
        return choose_difficulty_level()


def find_indexes(word, letter):
    indexes = []
    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes


def show_left_lifes(number_of_lives, user_word, used_letters):
    print()
    print(user_word)
    print("Used letters:", used_letters)
    print("Tries left", number_of_lives)
    print()


def letter_test(used_letters):
    letter = input("Enter a letter: ").lower()
    if letter.isalpha() and len(letter) == 1 and letter not in used_letters:
        used_letters.append(letter)
        return letter
    if letter.isdigit():
        print('A digit was entered:')
        return letter_test(used_letters)
    if letter in used_letters:
        print("This letter was used:")
        return letter_test(used_letters)
    else:
        print("Incorrect value:")
        return letter_test(used_letters)


def run_game():
    word_list = words.words()
    word = random.sample(word_list, 1)[0].lower()

    number_of_lives = choose_difficulty_level()
    print("lifes number:", number_of_lives)

    used_letters = []
    user_word = []

    for _ in word:
        user_word.append("_")

    while True:
        letter = letter_test(used_letters)

        found_indexes = (find_indexes(word, letter))
        if len(found_indexes) == 0:
            print("There is no such letter")
            number_of_lives -= 1

            if number_of_lives == 0:
                print("Game Over")
                break

        else:
            for index in found_indexes:
                user_word[index] = letter

            if "".join(user_word) == word:
                print("You win")
                break

        show_left_lifes(number_of_lives, user_word, used_letters)


def main():
    while True:
        run_game()

        run_again = input("If you want to play again, type: 'tak': ")

        if run_again != 'yes':
            break


if __name__ == '__main__':
    main()
