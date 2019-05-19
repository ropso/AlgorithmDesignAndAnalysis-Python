import sys
input()
li=list(map(int,input().split(" ")))
li.sort()
day=1
for i in range(0,len(li)):
    if li[i]>=day:
        day+=1
    else:
        pass
print(day-1)
stdout.input()
