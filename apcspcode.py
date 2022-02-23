'''
Hangman!!
'''
import random

def display(word, wrong, right): #displays the hangman status and guessed letters at the end of each turn
    correctword = True # this boolean checks if the whole word was guessed
    #prints the correct letters that have been guessed and '_' for the missing letters
    for x in range(len(word)):
        if (word[x] in right):
            print (word[x], end = '')
        else:
            print ('_', end = '')
            correctword = False
    print('\n')

    hangman = ["   +---+\n       |\n       |\n       |\n      ===", "   +---+\n   O   |\n       |\n       |\n      ===", "   +---+\n   O   |\n   |   |\n       |\n      ===", "   +---+\n   O   |\n  /|   |\n       |\n      ===", "   +---+\n   O   |\n  /|\  |\n       |\n      ===", "   +---+\n   O   |\n  /|\  |\n  /    |\n      ===", "   +---+\n   O   |\n  /|\  |\n  / \  |\n      ==="]
    print(hangman[len(wrong)]) #function for displaying hangman

    if (len(wrong) > 0):
        print("Incorrect letters: ", end = ' ') #prints all the wrong guessed letters
        for i in wrong:
            print(i, end = ' ')
    print('\n')

    return correctword

def inputletter (wrong, right): # gets in a inputted letter that has not been guessed before
    print('Guess a letter (make sure it is only 1 lower case letter):')
    letter = input()
    while ((len(letter) != 1) or (letter.isalpha() == False) or (letter in wrong) or (letter in right)):
        print('Input was incorrect. Make sure it is a single letter that you have not guessed before, Try Again:')
        letter = input()
    letter = letter.lower()
    return letter

def completeguessing(word):
    print('_' * len(word))
    won = False
    right = [] #correct letters guessed
    wrong = [] #incorrect letters guessed
    while(won == False and len(wrong) < 6):
        letter = inputletter(wrong, right)
        if (letter in word):
            right.append(letter)
        else:
            wrong.append(letter)
        if (len(wrong) > 6):
            break
        won = display(word, wrong, right)

    if (won == True):
        print("Great Job, You guessed the word! The word is quite hard so look it up and find out what it means!")
    else:
        print("Oh no, you ran out of turns :( The word was difficult so look it up and find out what it means!")

def wordgame():
    print("Hi! Welcome to My Hangman Game! \nThe rules are pretty simple: As prompted, input different letters in order to guess the mystery word that has been randomly generated! If your letter is correct, the letter will show up to replace the blanks. If your guess is is incorrect, you will lose a life. Once you have lost all 6 lives, you lose the game :( but if you complete the word before you lose your lives, you win :) Have fun playing!!\n")

    wordlist = 'aberration accolade acrimony angst anomaly antidoe baroque boondoggle bourgeois bravado cacophony capricious charisma dichotomy disheveled elan epitome equivocate euphemism fiasco finagle gregarious harbinger heresy idiosyncratic idyllic infinitesimal insidious junket kitsch litany lurid malaise malinger mantra mercenary misnomer narcissist nirvana oblivion ogle ostracize panacea paradox revel rhetoric spartan stoic suave teetotaler tirade ubiquitous untenable vicarious vile zealous'.split()
    word = wordlist[random.randint(0, len(wordlist) - 1)]

    completeguessing(word)
    print("Thank you for playing, I hope you had fun!!!")

wordgame()
