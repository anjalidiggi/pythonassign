"""
Assignment 1 Problem Statement :-
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

"""
# Enter the number of command which we wan to validate for all list opertaion
N = int(input("Enter the number of command"))
# define empty list
my_list = []
for _ in range(N):
        command = input("Enter Command Name with Value :- ").split()
        if command[0] == "insert":
            my_list.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(my_list)
        elif command[0] == "remove":
            my_list.remove(int(command[1]))
        elif command[0] == "append":
            my_list.append(int(command[1]))
        elif command[0] == "sort":
            my_list.sort()
        elif command[0] == "pop":
            my_list.pop()
        elif command[0] == "reverse":
            my_list.reverse()
"""
"insert 0 5": This will insert the value 5 at index 0.
"print": This will print the current list.
"remove 5": This will remove the value 5 from the list if it exists.
"append 10": This will append the value 10 to the end of the list.
"sort": This will sort the list in ascending order.
"pop": This will remove and return the last element from the list.
"reverse": This will reverse the elements of the list.
"""