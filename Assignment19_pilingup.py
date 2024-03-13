
"""
Problem Statement : -
There is a horizontal row of n cubes. The length of each cube is given.
 You need to create a new vertical pile of cubes.
 The new pile should follow these directions: if  is on top of  then .

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube
each time. Print Yes if it is possible to stack the cubes. Otherwise, print No.
"""
"""
Sample Output :-
input :-
2
6
4 3 2 1 3 4
output:-

Yes
input:-
3
1 3 2
No
"""


def can_stack_cubes(n, cubes):
    left = 0
    right = n - 1
    prev_cube = float('inf')

    while left <= right:
        if cubes[left] <= cubes[right]:
            if cubes[right] <= prev_cube:
                prev_cube = cubes[right]
                right -= 1
            else:
                return "No"
        else:
            if cubes[left] <= prev_cube:
                prev_cube = cubes[left]
                left += 1
            else:
                return "No"

    return "Yes"

T = int(input())
for _ in range(T):
    n = int(input())
    cubes = list(map(int, input().split()))
    result = can_stack_cubes(n, cubes)
    print(result)