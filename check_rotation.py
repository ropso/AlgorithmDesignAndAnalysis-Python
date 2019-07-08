from math import sqrt
li=[]
n=68
for i in range(1,int(sqrt(n)+1)):

    for j in range(1,int(sqrt(n)+1)):
    
        if i**2+j**2 == n:
        
            li.append([i,j])

print(li)