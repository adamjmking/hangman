import sys
import random

words = """ant baboon badger bat bear beaver camel cat clam cobra cougar
       coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
       lion lizard llama mole monkey moose mouse mule newt otter owl panda
       parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
       skunk sloth snake spider stork swan tiger toad trout turkey turtle
       weasel whale wolf wombat zebra""".split()
images = ['''
    +---+
        |
        |
        |
       ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ==='''] 
    
cheat = False
    
def play():
    randomWord = getRandomWord(words)
    blanks = list("_" * len(randomWord))
    parts = 0
    if cheat:
        print(randomWord)
    
    while True:
        # Detect loss
        if (parts > 5):
            choice = input(f"{images[6]} You Lose! The word was {randomWord.upper()} \n Would you like to play again? (y/n) ")
            if (choice == "y"):
                play()
            else:
                sys.exit(0)
        
        # Guess a letter
        s = "".join(blanks)
        letter = input(f"{images[parts]} {s} \n Guess a letter: ")
        if (letter not in randomWord):
            parts += 1
        else:
            for xx, char in enumerate(randomWord):
                if char == letter:
                    blanks[xx] = letter
          
        # Win detection  
        if ("_" not in blanks):
            choice = input(f"~~ You win! The word was {randomWord.upper()} ~~ \n Would you like to play again? (y/n) ")
            if (choice == "y"):
                play()
            else:
                sys.exit(0)
            
def getRandomWord(wordList):
    return wordList[random.randint(0, len(words) - 1)]

play()
