import os
import random

class Megaword:
    def __init__(self):
        self.directory = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.answer = ""
        self.player = ""
        self.games_played = 0
        self.wins = 0
        self.accuracy = 0
        self.guess_total = 0
        self.guess_avg = 0

    def word_pool(self):
        file = open(os.path.join(self.directory, "words"))
        count = 0
        for line in file:
            if line != "\n":
                count += 1
        file.close()
        return count

    def word(self):
        file = open(os.path.join(self.directory, "words"))
        pool = self.word_pool()
        g = random.randint(0, pool)
        read = file.readlines()
        self.answer = read[g]
        self.answer = self.answer.replace("\n", "")
        #print(self.answer)
        file.close()

    def play(self):
        print("______________________")
        self.word()
        attempts = 0
        solved = 0
        while attempts < 5:
            if solved == 1:
                print("***CORRECT***")
                break
            elif solved == -1:
                print("INVALID INPUT---- GAMEOVER")
                break
            else:
                guess = input("Guess %d: " % (attempts + 1)).lower()
                attempts += 1
                solved = self.input_checker(guess)

        if solved == 1 and attempts == 5:
            print("***CORRECT***")
        print("The word was: %s\n" % self.answer)
        input("Press Enter to return to menu\n")
        self.games_played += 1
        self.guess_total += attempts

    def input_checker(self, guess):
        guess = guess.lower()
        if len(guess) != 6:
            return -1
        elif not guess.isalpha():
            return -1
        elif guess == self.answer:
            self.wins += 1
            print("         %s" % self.feedback(guess))
            return 1
        else:
            print("         %s" % self.feedback(guess))

    def feedback(self, guess):
        feedback = ""
        i = 0
        for letter in guess:
            if guess[i] == self.answer[i]:
                feedback += "1"
            elif self.wrong_place(letter):
                feedback += "#"
            else:
                feedback += "0"
            i += 1
        return feedback

    def wrong_place(self, letter):
        i = 0
        wp = False
        while i < 5:
            if self.answer.find(letter, i, len(self.answer)) > -1:
                wp = True
            i += 1
        return wp

    def stats(self):
        print("\n_______________________")
        print("Player Stats")
        print("Player: %s" % self.player)
        print("Games Played: %s" % self.games_played)
        print("Wins: %s" % self.wins)
        if self.games_played != 0:
            self.accuracy = (self.wins / self.games_played) * 100
            self.guess_avg = self.guess_total / self.games_played
        print("Avg Guesses Per Game: %s" % self.guess_avg)
        print("Accuracy: %s %%" % self.accuracy)
        print("_______________________")
        input("Press Enter to return to menu\n")

    def info(self):
        print("****************************")
        print("Code Author: Megan Devereux")
        print("****************************")

        print("Game Instructions")
        print("The object of the game is to guess the correct 6 letter word")
        print("Each player is given 5 guesses per round")
        print("When a guess is submitted, a string of characters will appear beneath the guess")
        print("The index of the string correlates to the index of the player's guess")
        print("A 0 indicates that the letter is not in the world")
        print("A # indicates that the letter is in the word but in the incorrect position")
        print("A 1 indicates that the letter is in the word")
        print("The word will be revealed either after it is guessed correctly or if all 5 "
              "guesses are used")
        print("****************************")
        print("Program idea inspired by Wordle created by Josh Wardle\n")
        print("****************************")
        print("Thanks for Playing :)")
        print("****************************")
        input("Press Enter to return to menu\n")

game = Megaword()
run = True
input("Welcome! Press enter to set up profile.")
game.player = input("Enter your name: ")
while run:
    print("*****************")
    print("Megaword")
    print("The 6 Letter Word Game")
    print("*****************")
    user_input = input("(1) Play \n(2) Stats \n(3) Info \n(4) Quit\n ")
    if (user_input == "1"):
        game.play()
    elif (user_input == "2"):
        game.stats()
    elif(user_input == "3"):
        game.info()
    elif (user_input == "4"):
        confirm = input("Are you sure you want to quit? (Y/N) ").upper()
        if confirm == "Y":
            print("Thanks For Playing :) ")
            run = False
    else:
        print("INVALID INPUT!")

