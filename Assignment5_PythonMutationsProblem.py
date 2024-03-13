'''
Read a given string, change the character at a given index and then print the modified string.
Function Description

Complete the mutate_string function in the editor below.

mutate_string has the following parameters:

string string: the string to change
int position: the index to insert the character at
string character: the character to insert
Returns

string: the altered string
'''
def modify_string_using_list(s, index, new_char):
    # Convert the string to a list
    s_list = list(s)
    # Change the character at the given index
    s_list[index] = new_char
    # Join the list back to a string
    modified_string = ''.join(s_list)
    return modified_string

def modify_string_using_slice(s, index, new_char):
    # Slice the string and join it back after modification
    modified_string = s[:index] + new_char + s[index+1:]
    return modified_string

input_string = input("Enter the string: ")
index = int(input("Enter the index to modify: "))
new_char = input("Enter the new character: ")

# Method 1: Modify string using list
modified_string_list = modify_string_using_list(input_string, index, new_char)
print("Modified string using list method:", modified_string_list)

# Method 2: Modify string using slice
modified_string_slice = modify_string_using_slice(input_string, index, new_char)
print("Modified string using slice method:", modified_string_slice)

'''
Sample output :-
Enter the string: anjali
Enter the index to modify: 3
Enter the new character: L
Modified string using list method: anjLli
Modified string using slice method: anjLli

'''