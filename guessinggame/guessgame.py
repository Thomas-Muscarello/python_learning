#Have a secret word that the user needs to guess. Continue to guess until correct.

secret_word = "beer"
guess = ""
guess_count = 0
guess_limit = 3
gameover = False

#use while loop to continue to ask the question until the answer is correct.

while guess != secret_word and not(gameover):
    #Check to see if user has more guess'
    if guess_count < guess_limit:
        guess = input("Enter your guess of the 'secret word': ")
        guess_count += 1
    else:
        gameover = True

if gameover:
    print("You are out of guesses... GAMEOVER")
else:
    print("You Win!")