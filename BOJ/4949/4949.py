import sys
input = sys.stdin.readline
import re 

# 괄호들만 있는 문자열을 인자로 받아서 유효한 괄호인지 판단하는 함수
def is_valid(s):
    if len(s) == 0:
        return True
    stack = []
    table = {')':'(', ']':'['}
    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False
    return len(stack) == 0

# strings에 문자열들을 입력받아 리스트형태로 저장한다. 
strings = []
while True:
    s = input().rstrip()
    if s == '.':
        break
    strings.append(s)
    
# 입력받은 문자열들에서 괄호들만 new_strings에 담는다. 
new_strings = []
for s in strings:
    new_strings.append(re.sub('[0-9a-zA-Z .]', '', s))
    
for s in new_strings:
    if is_valid(s):
        print("yes")
    else:
        print("no")


