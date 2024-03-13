"""
Problem Statement : -
You are given an integer N followed by N email addresses. Your task is to print a list containing only valid email addresses in lexicographical order.

"""
"""
Sample Output :-
input:- 
3
anjali@diggibyte.com
gaytri@diggibyte.com
laxmi@diggibyte.com
output:-
['anjali@diggibyte.com', 'gaytri@diggibyte.com', 'laxmi@diggibyte.com']

"""
import re
def is_valid_email(email):
    pattern = r'^[\w-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    return bool(re.match(pattern, email))

N = int(input())
emails = [input().strip() for _ in range(N)]

valid_emails = sorted(filter(is_valid_email, emails))
print(valid_emails)