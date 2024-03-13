
"""
Problem Statement : -
You are given n words. Some words may repeat.
 For each word, output its number of occurrences.
  The output order should correspond with the input order of appearance of the word.
   See the sample input/output for clarification.

Note: Each input line ends with a "\n" character.
"""
"""
Sample Output :-
input :-
4
bcdef
abcdefg
bcde
bcdef

output:-

3
2 1 1
"""
from collections import OrderedDict

n = int(input())
words = [input().strip() for _ in range(n)]

word_count = OrderedDict()
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

distinct_words = len(word_count)
occurrences = list(word_count.values())

print(distinct_words)
print(*occurrences)