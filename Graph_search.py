"""
a b
b c
b d
d a
q w
q t
a s
a w
w e
w p
q a
find reachability
"""
li=list(map(int,input().split(" ")))
grapg_dict=dict()

for i in li:
    if grapg_dict.get(i[0]):
        grapg_dict[i[0]].append(i[1])
    else:
        grapg_dict[i[0]]=[]
        grapg_dict[i[0]].append(i[1])
print(grapg_dict)



