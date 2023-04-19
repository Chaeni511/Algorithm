# 균형잡힌 세상
import sys

while True:
    sentence = input()
    flag = 'yes'
    stack = []
    if sentence == '.':
        break
    else:
        for s in sentence:
            if s == '(' or s == '[':
                stack.append(s)

            elif s == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    flag = 'no'
                    break

            elif s == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    flag ='no'
                    break

        if stack:
            flag = 'no'

    print(flag)
