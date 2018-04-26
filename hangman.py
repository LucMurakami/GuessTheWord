import random
import json


class Hangman:

    def __init__(self):
        self.secret_word = self.make_word()
        self.display = list(self.secret_word)
        self.hide_display()
        self.play_game()

    def make_word(self):
        data = json.load(open('wordlist.json'))
        word_num = random.randint(0, 2642)
        return data['data'][word_num]

    def play_game(self):
        print('Would you like to play Hangman? (Yes or No)')
        player_input = input()
        misses = 0

        while player_input not in ('No', 'no'):
            print('There are ' + str(len(self.secret_word)) + ' letters in the secret word.')
            while misses <= 6:
                if misses < 6:
                    print('You have ' + str(7 - misses) + ' misses left.')
                elif misses == 6:
                    print('You have 1 miss left')

                if not self.guess_turns():
                    misses += 1

                if '?' not in str(self.display):
                    break

            if '?' not in str(self.display):
                print('\nCongratulations! You have won!')
            else:
                print('\nSorry, the word was ' + self.secret_word + '.')
                print('Better luc next time!')

            print('\nWould you like to play Hangman again? (Yes or No)')
            player_input = input()
            misses = 0

    def guess_turns(self):
        letter_entered = False
        while not letter_entered:
            print('\nGuess a letter')
            character_guess = input()
            try:
                if len(character_guess) == 1 and character_guess.isalpha():
                    if character_guess in self.secret_word:
                        print('Correct! That letter is in the secret word.')
                        self.add_chr(character_guess)
                        letter_entered = True
                        return True
                    else:
                        print('Sorry that letter is not in the word')
                        self.display_word()
                        letter_entered = True
                        return False
                else:
                    print('Please enter a letter')
            except ValueError:
                print('Please enter a letter')


    def hide_display(self):
        for i in range(len(self.secret_word)):
            self.display[i] = '?'

    def add_chr(self, character):
        secret_list = list(self.secret_word)

        for index in (range(len(self.secret_word))):
            if character is secret_list[index]:
                self.display[index] = character

        self.display_word()

    def display_word(self):
        for char in list(self.display):
            print(char, end=' ')
        print('')


Hangman()
