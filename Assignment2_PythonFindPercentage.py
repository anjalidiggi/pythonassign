'''
The provided code stub will read in a dictionary containing key/value pairs of
name:[marks] for a list of students.
 Print the average of the marks array for the student name provided,
  showing 2 places after the decimal.

The query_name is 'beta'. beta's average score is .

'''
n = int(input("Enter the number of students: "))
student_marks = {}
for _ in range(n):
    name, *line = input("Enter student name and marks: ").split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input("Enter the name of the student to calculate average score: ")

if query_name in student_marks:
    avg_score = sum(student_marks[query_name]) / len(student_marks[query_name])
    print("{:.2f}".format(avg_score))
else:
    print("Student name not found.")
'''
output format 
Enter the number of students: 3
Enter student name and marks: gaytri 90 80 70
Enter student name and marks: laxmi 60 70 89
Enter student name and marks: kalluri 50 80 90
Enter the name of the student to calculate average score: laxmi
73.00
'''