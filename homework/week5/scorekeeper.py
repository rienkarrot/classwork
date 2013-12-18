SCORE_CARD = {}

test_numbers = [{"name": "enne",
            "scores": [-1, 10, -5]}
            {"name": "naomi",
            "scores": [-5, -3, 25]}
            {"name": "violet",
            "scores": [15, -2, -3]}]

try:
    with open("scores.txt") as f:
        for line in f:
    #function that reads each line and adds players and scores
except IOError:
    print 'There is no file named' , f

def populate_score_card(test_numbers):
    SCORE_CARD = copy.deepcopy(test_numbers)
    for i in SCORE_CARD:
        i["scores"] = SCORE_CARD[i["scores"]]
    return SCORE_CARD

#need to add and print current totals
def add_scores(SCORE_CARD["scores"]):
    total = 0
    for key in SCORE_CARD["scores"]:
        total += score[i]
    return total
    
def print_scores(x):
    print 'Total points per player: %s' % x