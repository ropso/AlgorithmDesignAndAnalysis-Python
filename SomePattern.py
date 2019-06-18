num=int(input())
a=[2,3,4,5,6]

for elem in range(1,num+1):
    patern=list(map(str,[elem]*elem))
    patern="*".join(patern)
    print(patern)
for elem in range(num,0,-1):
    patern=list(map(str,[elem]*elem))
    patern="*".join(patern)
    print(patern)    