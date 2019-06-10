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
li=[]
for i in range(0,11):
    li.append(list(map(str,input().split(" "))))
grapg_dict=dict()

for i in li:
    print(i)
    if grapg_dict.get(i[0])!=None:
        grapg_dict[i[0]].append(i[1])
    else:
        grapg_dict[i[0]]=[]
        grapg_dict[i[0]].append(i[1])
print(grapg_dict)

# print all path to reach w from a 

#bfs
#dfs
finding='Z'
start='a'
stacklist=[start]
Quelist=[start]
traversedset=set()
while(len(Quelist)!=0):
    #todo add all connectin elemnts 
    if Quelist[0]==finding:
        print('wegot a path')
        break
    elif Quelist[-1] not in traversedset:
        vertex=Quelist.pop()
        if grapg_dict.get(vertex)!=None:
            for elem in grapg_dict[vertex]:
                Quelist.append(elem)
        traversedset.add(vertex)
        print(vertex)
    else:
        print("No PAth")
        break



