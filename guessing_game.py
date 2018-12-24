from random import  *
#creatin a list
guess_store = []
#creating an empty variable
best_score = 0
#creating function to store guesses
def guesses(guess_input):
    guess_store.append(guess_input)
#creating function to store the lowest score
def reset(score):
    print("""
    The best score is {}! Can you beat it?""".format(score))
    guess_store.clear()
#creating a while loop to repeat when the user wants to play again
while True:
    random_store = randint(1,10)
    print("""
    ********************************

    Welcome to the "GUESSING GAME!!"

    ********************************
    For help type 'HELP'
    """)
#creating a "try", "except" for invalid entries (non-numeric)
    try:
        guess = int(input("Go ahead, pick a number. "))
        guesses(guess)
#creating a while loop to repeat when the user guesses the wrong number
        while guess != random_store:
            guesses(guess)
            if guess < random_store:
                guess = int(input("Sorry, too low! Try again. "))
                continue
            if guess > random_store:
                guess = int(input("Sorry, too high! Try again. "))
                continue
    except ValueError as err:
        print("Entry must be a number, please try again. ErrorType:'{}'".format(err))
        continue
#creating a screen prompt to notify the user of the number of attempts and whether they would like to play again
    repeat = input("""
    You got it!! It took you {} attempts.
    Would you like to play again? ['Y']es / ['N']o """.format(len(guess_store))).upper()
#if they type 'Y' then the first while loop will repeat
    if repeat == 'Y':
        if  best_score is 0:
            best_score = len(guess_store)
            reset(best_score)
            continue
        if len(guess_store) <= best_score:
            best_score = len(guess_store)
            reset(best_score)
            continue
        if len(guess_store)>= best_score:
            best_score = best_score
            reset(best_score)
            continue
#if they select 'N' the game will end
    if repeat =='N':
        print("Thaks for playing.")
        break
# if they type anyting other than a 'Y' or 'N' they will be prompted and the game will end
    else:
        print("You must type 'Y' or 'N' only ")
        break
