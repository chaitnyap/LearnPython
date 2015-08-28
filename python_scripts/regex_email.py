import re
'''
regex to validate email
Input Format:
An integer N followed by N lines containing a string
Constraints:
Each of the line is a non-empty string.
Output Format:
A list containing valid email addresses in lexicographic order. If the list is empty, just output an empty list, [].
'''
#n = input()
#e = [raw_input().strip() for _ in range(n)]
n = 3
e = ['lara@hackerrank.com', 'brian-23@hackerrank.com', 'britts_54@hackerrank.com', '123@aaa.com', 'a1234', 'b1@a.co', 'b11@a.co', 'zzzz@.coi', 'ha@git@int.cz', 'fjladfk_iasdfad234@sdlkjf23335.in', 'prashant24_@gmail.com']
regex = re.compile(r'^[a-z][\w-]*\@[a-z0-9]+\.[a-z]{1,3}$')
ve = filter(lambda email: regex.search(email), e)
ve.sort()
print ve
