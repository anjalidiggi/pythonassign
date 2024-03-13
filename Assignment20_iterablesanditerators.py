
"""
Problem Statement : -
The itertools module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination. Together, they form an iterator algebra making it possible to construct specialized tools succinctly and efficiently in pure Python.

To read more about the functions in this module, check out their documentation here.

You are given a list of N lowercase English letters. For a given integer N, you can select any K indices (assume 1-based indexing) with a uniform probability from the list.

Find the probability that at least one of the K indices selected will contain the letter: ''.

"""
"""
Sample Output :-
input:-
Enter the count of lower case latter :-4
a a c d
2
output :- 
0.8333
"""
from itertools import combinations

N = int(input("Enter the count of lower case latter :-"))
letters = input().split()
K = int(input())

total_combinations = list(combinations(range(1, N + 1), K))
favorable_combinations = [comb for comb in total_combinations if 'a' in [letters[i - 1] for i in comb]]

probability = len(favorable_combinations) / len(total_combinations)
print("{:.4f}".format(probability))