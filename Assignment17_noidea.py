"""
Problem Statement : -
There is an array of  integers. There are also  disjoint sets,  A and B , each containing m  integers. You like all the integers in set  A and dislike all the integers in set B . Your initial happiness is 0 . For each i integer in the array, if i A , you add  to your happiness. If , you add  to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since  and  are sets, they have no repeated elements. However, the array might contain duplicate elements.

Constraints



Input Format

The first line contains integers n  and  m separated by a space.
The second line contains  n integers, the elements of the array.
The third and fourth lines contain m  integers,  A and B , respectively.

Output Format

Output a single integer, your total happiness.

"""
"""
Sample Output :-
INPUT:- 
3 2 
1 5 3
3 1
5 7
OUTPUT"-
1
"""
n, m = map(int, input().split())
array = list(map(int, input().split()))
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

happiness = sum((i in set_a) - (i in set_b) for i in array)
print(happiness)