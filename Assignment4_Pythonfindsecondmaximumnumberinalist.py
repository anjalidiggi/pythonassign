'''
Given the participants' score sheet for your University Sports Day
, you are required to find the runner-up score. You are given  scores
. Store them in a list and find the score of the runner-up.

'''
# Taking input of scores separated by space and converting them into integers
scores = list(map(int, input("Enter scores separated by space: ").split()))

# Removing duplicates and sorting the list in descending order
unique_scores = sorted(set(scores), reverse=True)

# If there are less than two unique scores, there is no runner-up
if len(unique_scores) < 2:
    print("No runner-up score")
else:
    # The runner-up score is the second highest score
    runner_up_score = unique_scores[1]
    print("Runner-up score:", runner_up_score)
'''
sample output :-
Enter scores separated by space: 5 4 9 2 8 1 6
Runner-up score: 8
'''