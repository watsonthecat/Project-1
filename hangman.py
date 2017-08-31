import random


WORDLIST_FILENAME = "words.txt"

#create Hangman class
class Hangman():
    #the _init_ function is called a constructor/initializer
    #it is automatically called when you create a new instance of a class
    #within that function, the newly created object is assigned to the parameter self

    #print("Is this is a thing?")
    wordList = [""]
    def _init_(self):


        print("Hangman: Stick man's life depends on you!")
        print("Are you ready to play?")
        print("If you are ready to play enter: 1")
        print("If you can't handle the pressure: 2")
        usr_input = input()

        if usr_input == '1':
            #If the user enters 1, start the game
            self.start_game()

        elif usr_input == '2':
            #If the user enters 2, exit the game
            print("Goodbye!")
            exit()
        else:
            print("I'm sorry, could you repeat that?")
            self._init_()

    def loadWords(self):

        #Returns a list of valid words: Words are strings of lowercase letters

        #opens the given text file in READ mode
        #The first argument is a string containing the filename.
        #The second argument is another string containing a few characters describing the way in which the file will be used.
        #mode can be 'r' when the file will only be read, 'w' for only writing (an existing file with the same name will be erased),
        # and 'a' opens the file for appending; any data written to the file is automatically added to the end.
        #'r+' opens the file for both reading and writing. The mode argument is optional;
        #'r' will be assumed if it’s omitted.
        file = open(WORDLIST_FILENAME, 'r')
        line = file.readline()
        wordList = str.split(line)
        #with open(WORDLIST_FILENAME, 'r') as f:
        #    wordList = [line.strip() for line in f]
        print("",len(wordList),"words loaded")
        self.wordList = wordList

        return wordList

    def chooseWord(self,wordList):

        x = random.choice(self.wordList)
        # for testing
        #print(self.wordList[0])
        return x

    def start_game(self):
        print("You have the chance to save this sorry soul")
        print("If you make 6 wrong guesses, we hang the man!")
        self.core_game()


    def is_word_guessed(self, theWord, lettersUsed):

        #theWord: string, the word the user is guessing
        #lettersUsed: list of letters guessed so far
        #returns: boolean, True if all the letters of theWord are in lettersUsed; false otherwise

        count = 0

        for i, c in enumerate(theWord):
            if c in lettersUsed:
                count +=1
        if count == len(theWord):
            return True
        else:
            return False

    def core_game(self):

        self.loadWords()

        guesses = 0
        lettersUsed = ""
        #make an array of words to choose from, to add more words/multiple plays
        theWord = self.chooseWord(self.wordList)
        print("THE WORD IS: ",theWord)
        #if array of words, progress size would equal word[x].length
        progress = ["?","?","?","?","?"]
        wordGuessed = False


        while guesses < 6 and wordGuessed is False:
            guess = input("Guess a letter: ")

            #if their guess is correct
            if guess in theWord and guess not in lettersUsed:

                print("You guessed correctly!")

                #add guess to lettersUsed
                lettersUsed += guess + ","

                #this is where you win the game.......
                wordGuessed = self.is_word_guessed(theWord,lettersUsed)
                if wordGuessed == True:
                    guesses = 99

                #call hangman graphic, sending # of guesses
                self.hangman_graphic(guesses)

                #display progress
                print("Progress: " + self.progress_updater(guess,theWord,progress))
                #display letters used
                print("Letter used: " + lettersUsed)


            #if their guess is incorrect
            elif guess not in theWord and guess not in lettersUsed:
                guesses += 1
                print("WRONG answer!! I thought you value life!")
                lettersUsed += guess + ","
                self.hangman_graphic(guesses)
                print("Progress: " + "".join(progress))
                print("Letter used: " + lettersUsed)

            elif guess in lettersUsed:
                print("You have already guessed that letter!")
            else:
                print("Is that even a letter? Try again...")

#python should be writing to a standard buffer, flush makes sure it's empty before you use it again
#was getting an error so I put it on every line 
    def hangman_graphic(self, guesses):
        if guesses == 0:
            print ("________      ", flush = True)
            print ("|      |      ", flush = True)
            print ("|             ", flush = True)
            print ("|             ", flush = True)
            print ("|             ", flush = True)
            print ("|             ", flush = True)
        elif guesses == 1:
            print ("________      ", flush = True)
            print ("|      |      ", flush = True)
            print ("|      0      ", flush = True)
            print ("|             ", flush = True)
            print ("|             ", flush = True)
            print ("|             ", flush = True)
        elif guesses == 2:
            print ("________      ", flush = True)
            print ("|      |      ", flush = True)
            print ("|      0      ", flush = True)
            print ("|     /       ", flush = True)
            print ("|             ", flush = True)
            print ("|             ", flush = True)
        elif guesses == 3:
            print ("________      ", flush = True)
            print ("|      |      ", flush = True)
            print ("|      0      ", flush = True)
            print ("|     /|      ", flush = True)
            print ("|             ", flush = True)
            print ("|             ", flush = True)
        elif guesses == 4:
            print ("________      ", flush = True)
            print ("|      |      ", flush = True)
            print ("|      0      ", flush = True)
            print ("|     /|\     ", flush = True)
            print ("|             ", flush = True)
            print ("|             ", flush = True)
        elif guesses == 5:
            print ("________      ", flush = True)
            print ("|      |      ", flush = True)
            print ("|      0      ", flush = True)
            print ("|     /|\     ", flush = True)
            print ("|     /       ", flush = True)
            print ("|             ", flush = True)

        elif guesses == 99:
            print ("________                    ", flush = True)
            print ("|      |                    ", flush = True)
            print ("|                           ", flush = True)
            print ("|    \ 0 / - Wooohoo!Thanks!", flush = True)
            print ("|      |                    ", flush = True)
            print ("|     / \                   ", flush = True)
            print("CONGRATULATIONS YOU FREAKING WON!")
            self._init_()
        else:
            print ("________      ", flush = True)
            print ("|      |      ", flush = True)
            print ("|      0      ", flush = True)
            print ("|     /|\     ", flush = True)
            print ("|     / \     ", flush = True)
            print ("|             ", flush = True)
            print ("The noose tightens around his neck!", flush = True)
            print ("HIS LIFE IS ON YOU, MONSTER!.", flush = True)
            print ("YOU LOOSE -- GAME OVER!", flush = True)
            self._init_()

    def progress_updater(self, guess, theWord, progress):
        i = 0

        while i < len(theWord):
            if guess == theWord[i]:
                progress[i] = guess
                game.correctAnswer = str("".join(progress))
                i += 1
            else:
                i += 1

        return "".join(progress)


game = Hangman()
game._init_()
#the _init_ function is called a constructor/initializer
#it is automatically called when you create a new instance of a class
#within that function, the newly created object is assigned to the parameter self
