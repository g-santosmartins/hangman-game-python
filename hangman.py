import random


def play():
  wish_to_play = True
  #main logic
  while (wish_to_play == True):
    print_openning_msg()
    secret_word = load_secret_word()

    correct_words = get_correct_words(secret_word)
    print(correct_words)

    died = False
    get_it_right = False
    errors = 0

    while(not died and not get_it_right):

        guess = asks_guess()

        if(guess in secret_word):
            score_guess(guess, correct_words, secret_word)
        else:
            errors += 1
            draws_player(errors)

        died = errors == 7
        get_it_right = "_" not in correct_words

        print(correct_words)

    if(get_it_right):
        prints_winner_msg()
        decision = input("You killed it! Would you like to play more? Y/N:").lower()
        if(decision == "n" ):
          wish_to_play = False
        print(wish_to_play)
    else:
        prints_loser_msg(secret_word)
        decision = input("You lose! Would you like to try it again? Y/N:").lower()
        if(decision == "n" ):
          wish_to_play = False
        print(wish_to_play)

#functions

  
  
    
def draws_player(errors):
    print("  _______     ")
    print(" |/      |    ")

    if(errors == 1):
        print (" |      (_)   ")
        print (" |            ")
        print (" |            ")
        print (" |            ")

    if(errors == 2):
        print (" |      (_)   ")
        print (" |      \     ")
        print (" |            ")
        print (" |            ")

    if(errors == 3):
        print (" |      (_)   ")
        print (" |      \|    ")
        print (" |            ")
        print (" |            ")

    if(errors == 4):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |            ")
        print (" |            ")

    if(errors == 5):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |            ")

    if(errors == 6):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      /     ")

    if (errors == 7):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()



def prints_winner_msg():
    print("Great Job! You did it!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def prints_loser_msg(secret_word):
    print("Oh, what a shame, you were smothered!")
    print(f"The key word was {secret_word}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print(" /                   \  ")
    print(" |   XXXX     XXXX   |  ")
    print(" |   XXXX     XXXX   |     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def score_guess(guess, correct_words, secret_word):
    index = 0
    for letra in secret_word:
        if (guess == letra):
            correct_words[index] = letra
        index += 1

def asks_guess():
    guess = input("Type a letter and press ENTER: ")
    guess = guess.strip().upper()
    return guess

def get_correct_words(word):
    return ["_" for letter in word]

def print_openning_msg():
    print("*********************************")
    print("***Welcome to the HANGMAN GAME!***")
    print("v.0.0.1")
    print("Thanks for playing! It will make me happy if you drop by my Github: https://github.com/g-santosmartins ")
    print("*********************************")

def load_secret_word():
    file = open("words.txt", "r")
    words = []

    for line in file:
        line = line.strip()
        words.append(line)

    file.close()

    numero = random.randrange(0, len(words))
    secret_word = words[numero].upper()
    return secret_word


if(__name__ == "__main__"):
    play()
