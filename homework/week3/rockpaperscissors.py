def is_better_than(player0, player1):
    valid = ["rock", "paper", "scissors"]
    if player0 not in valid or player1 not in valid:
	    return None
    if player0 != player1:
        if player0 == "rock" and player1 == "paper":
	        return False
        elif player0 == "paper" and player1 == "scissors":
	        return False
        elif player0 == "scissors" and player1 == "rock":
            return False
        else:
            return True
    else:
        return None
    
	
print is_better_than("rock", "scissors")

"""
    Simulate a rock, paper, scissors game!

    Paper beats rock, scissors beats paper, rock beats scissors.

    This function only needs to consider strings as input.

    Parameters:

    player0 - a string (either "rock", "paper", or "scissors")
    player1 - a string (either "rock", "paper", or "scissors")

    Returns:
        True if player0 beats player1
        False if player1 beats player0
        None if a tie, or if an invalid string is passed
"""
pass
