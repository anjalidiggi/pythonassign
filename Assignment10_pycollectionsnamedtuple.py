"""
Problem Statement : -
Task

Dr. John Wesley has a spreadsheet containing a list of student's , ,  and .

Your task is to help Dr. Wesley calculate the average marks of the students.


Note:
1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.
2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)

Input Format

The first line contains an integer , the total number of students.
The second line contains the names of the columns in any order.
The next  lines contains the , ,  and , under their respective column names.

Constraints


Output Format

Print the average marks of the list corrected to 2 decimal places.
"""
"""
Sample Output :-
Total Number of Students :- 2
ID MARKS NAME CLASS
1 97 ANJALI 9
2 87 GAYTRI 8
92.00

"""


def calculate_average_marks(num_students, columns, data):
    marks_index = columns.index('MARKS')
    total_marks = sum(int(row[marks_index]) for row in data)
    return total_marks / num_students

num_students = int(input("Total Number of Students :- "))
columns = input().split()
data = [input().split() for _ in range(num_students)]

average_marks = calculate_average_marks(num_students, columns, data)
print("{:.2f}".format(average_marks))