
count = 0
all_guesses = []

while count < 6:
    guess = raw_input("Enter a number: ")
    count += 1
	all_guesses.append(guess)

print all_guesses.sort()
    
