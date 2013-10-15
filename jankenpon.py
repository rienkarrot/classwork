import random
teammate = finn

turns = 0

while turns < 6:
    player_choice = raw_input('')
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
	print "The computer/'s choice is:", computer_choice
	turns +=1
	
	
def compare(player_choice, computer_choice):
    if player_choice == computer_choice:
	    return "It's a tie!"
	elif player_choice == "rock" and computer_choice == "paper":
	    return "Computer!"
	elif player_choice == "paper" and computer_choice == "scissors":
	    return "Computer!"
	elif player_choice == "scissors" and computer_choice == "rock":
	    return "Computer!"
	else:
	    return "Player!"

print compare



for i in range(6):
    