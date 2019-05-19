no=input()
opeartions=input()
"""what we are trying to do 
on iteration ,stack is filled only by +
1>if stack empty ignore the -
2>if stack non empty pop +
answer would be no of elemnts in the stack
"""
stack=list()
for opration in opeartions:
    if opration=='-' and len(stack)==0:
        continue
    elif opration=='+':
        stack.append(1)
    else:
        stack.pop()
print(stack.__len__())
