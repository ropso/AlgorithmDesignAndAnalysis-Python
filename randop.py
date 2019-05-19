num=input()
num=int(num)
li=input().split(" ")
li=list(map(int,li))
intervallist=[]
ar_length=len(li)
for i in range(2,ar_length+1):
    jslow=0
    while((jslow+i)<ar_length):
        if abs(li[jslow]-li[jslow+i])<=num:
            intervallist.append([jslow,jslow+i])
        jslow+=1
print(intervallist)


