""" The Hangman game. """
# Hangman.py

# Information: A game where a user attempts to guess the letters of a random
# word selected by the computer opponent. The user will have a specific amount
# of tries to guess the letters. If the user is able to guess all the letters
# before the amount of tries run out, they win the game. If not, they lose.

import time
import random


class Hangman:
    """
    The Hangman game.
    """

    def __init__(self) -> None:
        """
        Initialize Hangman game.
        """
        
        print("You woke up one day to realize you've committed a heinous crime.")
        print("A crime like no other. May it be ruthless murder, senseless rape, ")
        print("hedonistic mutilation, or... even a royal assassination?")
        time.sleep(6)
        print("You don't know. All you know is that it's bad. Really bad.")
        print("...")
        time.sleep(2)
        print("Why, you ask?")
        time.sleep(2)
        print("Oh, for you are on a noose!")
        time.sleep(5)
        print("Welcome to Hangman. Do you want to save your life?")
        time.sleep(1)
        print("(Yes) I have been alive, and would like to keep it that way.")
        print("(No) For I am already dead inside.")
        user_choice = input("->")

        if user_choice == 'yes' or user_choice == 'Yes' or user_choice == 'YES':
            print("Ah, lovely how your life is about to depend on a word.")
            self.start_game()
        elif user_choice == 'no' or user_choice == 'No' or user_choice == 'NO':
            print("Yikes. Good luck on your afterlife...")
            exit()
        else:
            print("What was that? You have to choose either yes or no.")
            self.repeat_intro()

    def repeat_intro(self) -> None:
        """
        Repeat the  intro  if  user inputted an incorrect string.
        """
        print("Welcome to Hangman. Do you want to save your life?")
        time.sleep(1)
        print("(Yes) I have been alive, and would like to keep it that way.")
        print("(No) For I am already dead inside.")
        user_choice = input("->")

        if user_choice == 'yes' or user_choice == 'Yes' or user_choice == 'YES':
            print("Ah, lovely how your life is about to depend on a word.")
            self.start_game()
        elif user_choice == 'no' or user_choice == 'No' or user_choice == 'NO':
            print("Yikes. Good luck on your afterlife...")
            exit()
        else:
            print("What was that? You have to choose either yes or no.")
            self.repeat_intro()

    def start_game(self) -> None:
        """
        Outlines the instructions of the Hangman game.
        """

        time.sleep(2)
        print("...")
        print("You've regained most of your consciousness back.")
        print("It's a scary thing to end up on a noose one day, ")
        print("without any prior recollection. Oh, well, at least ")
        print("you're given the chance to live.")
        print("...")
        print("You are required to guess a word letter by letter.")
        print("If you guess it right within 6 tries, you win.")
        print("Else, you suffocate and die a measly death.")
        time.sleep(2)
        print("...")
        print("Delightful, right? Let's begin.")
        self.random_word()

    def random_word(self) -> None:
        """
        Randomly chooses a word from given word lists.
        """

        print(" ")
        print(" ")
        print("Choose your difficulty:")
        print("(1) Low (Cowardly, but safe bet.)")
        print("(2) Medium (Living on the edge?)")
        print("(3) High (Suicidal, are we?)")
        user_choice = input("->")
        
        ez_words = ['dead', 'life', 'flux', 'maze', 'eerie', 'done', 'fake', 'mask']
        med_words = ["hijacked", 'jumped', 'borrow', 'bullet', 'calmer', 'boozed']
        hard_words = ['serendipity', 'sublimity', 'resurrection', 'contentment']
        
        if user_choice == '1':
            word = random.choice(ez_words)
            self.execute_game(word)
        elif user_choice == '2':
            word = random.choice(med_words)
            self.execute_game(word)
        elif user_choice == '3':
            word = random.choice(hard_words)
            self.execute_game(word)
        else:
            print("What was that? You have to choose either 1, 2 or 3.")
            self.random_word()

    def execute_game(self, word: str, life_count: int=6, guessed: set=set()) -> None:
        """
        Execute the game with the randomly selected word. Correct guesses do
        consume lives whereas incorrect guesses do. End game when life count
        reaches 0.
        """

        # Check the number of remaining lives.
        print("You have " + str(life_count) + " lives remaining.")
        print("Choose wisely.")

        # Display letters that have already been guessed.
        if len(guessed) != 0:
            print("You have already guessed these letters:")
            print(guessed)

        # Displays the hangman art that corresponds to the life_count.
        self.hangman_art(life_count)

        # Displays the empty letters of the word.
        disp_word = ""
        for letter in word:
            if letter in guessed:
                # Do not hide the letter upon display.
                disp_word += " " + letter + " "
            else:
                # Hide the letter upon display.
                disp_word += " _ "

        # Print the word as it has been guessed so far.
        print("")
        print(disp_word)
        print("")

        # Check if the word has been guessed.
        if "_" not in disp_word:
            # The game is over.
            print("You win.")
            print("...")
            print("Wow... Didn't think you'd actually guess that.")
            print("I guess, it's time for you to go back to doing the life thing.")
            print("--x--")
            exit()
        else:
            # Asks the user to guess a letter.
            guess = input("Your guess: ")
            guessed.add(guess)

            # Check if the letter is contained in the word.
            if guess in word:
                print("That's correct.")
                self.execute_game(word, life_count, guessed)
            else:
                print("Nice try...")
                time.sleep(2)
                print("Not really.")
                time.sleep(2)
                # Changes game state, including life_count accordingly.
                life_count -= 1
                # Add guessed letter to the guessed set.
                if life_count == 0:
                    print("That was your last chance.")
                    print("Pray, for your time has come.")
                    self.hangman_art(life_count)
                else:
                    self.execute_game(word, life_count, guessed)

    def hangman_art(self, life_count) -> None:
        """
        Displays the hangman art corresponding to the amount of lives that the
        player has left.
        """

        if life_count == 6:
            print("________      ")
            print("|      |      ")
            print("|             ")
            print("|             ")
            print("|             ")
            print("|             ")
        elif life_count == 5:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|             ")
            print("|             ")
            print("|             ")
        elif life_count == 4:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /       ")
            print("|             ")
            print("|             ")
        elif life_count == 3:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|      ")
            print("|             ")
            print("|             ")
        elif life_count == 2:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\     ")
            print("|             ")
            print("|             ")
        elif life_count == 1:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\     ")
            print("|     /       ")
            print("|             ")
        else:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\     ")
            print("|     / \     ")
            print("|             ")
            print("I expected you to put up more of a fight.")
            print("What a disappointment...")
            print(" ")
            print(" ")
            self.restart_game()

    def restart_game(self) -> None:
        """
        Restart the game after GAME OVER.
        """
        print("I feel generous today. Want to restart?")
        print("(1) Mhmm.")
        print("(2) Nope. Death is for me.")
        user_choice = input("-> ")

        if user_choice == "1":
            self.repeat_intro()
        elif user_choice == "2":
            exit()
        else:
            print("What was that? You have to pick either 1 or 2.")
            self.restart_game()


game = Hangman()