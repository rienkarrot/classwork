import random

secret_num = random.randint(0,101)

while True:
    guess = raw_input("Enter a positive number up to 100: ")
    if guess > secret_num:
	    print "Too high! Try again."
	elif guess < secret_num:
	    print "Too low! Try again."
    else:
        print "You win!"
        break