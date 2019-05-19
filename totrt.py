ar=[4, 8, 15, 16, 23, 42]
lio=dict()
sand=[]
for i in range(0,6):
    for j in range(0,6):
        if (ar[i]*ar[j] in lio.keys() ) or (ar[i]*ar[j]in lio.keys()) or i==j:
            continue
        lio[ar[i]*ar[j]]=(ar[i],ar[j])
        sand.append(ar[i]*ar[j])

guess_ary=[]
print("? 1 2",flush=True)
x12=int(input())
xfactor12=lio[x12]
# print(xfactor12)
print("? 2 3",flush=True)
x23=int(input())
xfactor23=lio[x23]
# print(xfactor23)
common=0
for i in xfactor12:
    for j in xfactor23:
        if i==j:
            common=i
            break
try:
    guess_ary.append(x12//common)
except:
    print("0")
    exit()
guess_ary.append(common)
guess_ary.append(x23//common)
# print(guess_ary)

print("? 4 5",flush=True)
x45=int(input())
xfactor45=lio[x45]
# print(xfactor45)
print("? 5 6",flush=True)
x56=int(input())
xfactor56=lio[x56]
# print(xfactor56)
common=0
for i in xfactor45:
    for j in xfactor56:
        if i==j:
            common=i
            break
try:
    guess_ary.append(x45//common)
except:
    print('0')
    exit()
guess_ary.append(common)
guess_ary.append(x56//common)
print("!",end=" ")
print(*guess_ary,sep=" ")



