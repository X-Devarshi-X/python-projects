# Q9. Hangman
import random

def hangman(List):
    try:
        word = random.choice(List)
        if 0 <= List.index(word) <= 23:
            hint = "Sport"
        if 24 <= List.index(word) <= 96:
            hint = "Country"
        if 97 <= List.index(word) <= 142:
            hint = "Animal"
        your_guess = ""
        turns = 10
        while turns > 0:
            error = 0
            for c in word:
                if c in your_guess:
                    print(c, end=' ')
                else:
                    print("_", end=' ')
                    error += 1
            if error == 0:
                print('\nHurrah! You Won')
                break

            char = input('\nEnter : ')
            your_guess += char
            if char not in word:
                print('\nTry Again. ', end='')
                turns -= 1
                print('You have {} guesses left.'.format(turns))
                if turns == 3:
                    print("\nHint : {}".format(hint))
                if turns == 0:
                    print('\nYou Lose. The word was : ', word)
        game_over = 'Game Over'
    except KeyboardInterrupt:
        game_over = 'Bye! Try Again!'
    return game_over


L = ['football', 'cricket', 'basketball', 'baseball', 'volleyball', 'archery', 'handball', 'athletics', 'badminton', 'tennis', 'soccer', 'chess', 'wrestling',
     'gymnastics', 'cycling', 'skating', 'fencing', 'rowing', 'golf', 'polo', 'squash', 'javelin', 'kayaking', 'boxing', 'latvia', 'croatia',
     'france', 'italy', 'portugal', 'spain', 'england', 'hungary', 'luxemborg', 'armenia', 'russia', 'liechtenstein', 'germany', 'belgium', 'ukraine', 'lithuania',
     'sweden', 'finland', 'scotland', 'ireland', 'norway', 'poland', 'romania', 'belarus', 'kazakhstan', 'greece', 'bulgaria', 'iceland', 'austria', 'serbia',
     'slovakia', 'estonia', 'denmark', 'switzerland', 'netherlands', 'moldova', 'albania', 'turkey', 'slovenia', 'kosovo', 'cyprus', 'azerbaijan', 'montenegro',
     'brazil', 'ecuador', 'argentina', 'venezuela', 'colombia', 'peru', 'chile', 'bolivia', 'uruguay', 'paraguay', 'canada', 'mexico', 'haiti', 'cuba', 'jamaica',
     'panama', 'honduras', 'india', 'pakistan', 'japan', 'china', 'indonesia', 'thailand', 'philippines', 'singapore', 'vietnam', 'afghanistan', 'myanmar', 'israel', 'nepal',
     'octopus', 'fish', 'shark', 'lion', 'tiger', 'cheetah', 'panther', 'giraffe', 'elephant', 'rat', 'cat', 'dog', 'dolphin', 'anaconda', 'snake', 'alligator',
     'crocodile', 'ant', 'beetle', 'bison', 'camel', 'catfish', 'chicken', 'centipede', 'owl', 'vulture', 'eagle', 'butterfly', 'bee', 'mosquito', 'cow', 'deer', 'duck',
     'lizard', 'frog', 'fox', 'goat', 'gorilla', 'grasshopper', 'zebra', 'walrus', 'turkey', 'starfish', 'sardines', 'seahorse', 'rhinoceros']


hangman(L)

