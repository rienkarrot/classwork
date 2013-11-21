from markov import *

def whee(x):
'''
Next, use your new update_table function in conversation.py to build a
program that repeatedly:

- Asks the user for input
- Updates the table with the user's input
- Says something based on the table
- If the user ever types "bye", the program exits.
'''
    x = raw_input("Please type something here: ")
    while x != "bye"
        print table_of_next_words(x)
        
    
