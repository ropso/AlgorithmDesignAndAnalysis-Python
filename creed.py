""""
7 5
3 2 5 4
0
2 1 2
1 1
2 6 7
"""
def findDisjoint(common_elem,group,elem_list):
    group=set(group)
    elem_list=set(elem_list)
    tm=list(group-elem_list)
    tm.remove(common_elem)
    return tm

def getConnection(index):
    traversedset=set()
    finding=89
    Quelist=[index]
    while(len(Quelist)!=0):
        if Quelist[0]==finding:
            print('wegot a path')
            break
        elif Quelist[-1] not in traversedset:
            vertex=Quelist.pop()
            if Group_graph.get(vertex)!=None:
                for elem in Group_graph[vertex]:
                    Quelist.append(elem)
            traversedset.add(vertex)
        else:
            break;
    print(len(traversedset))
    



a,b=input().split(" ")
a=int(a)
group_list=[]
b=int(b)
Group_graph=dict()
for i in range(0,b):
    group_list.append(list(map(int,input().split(" ")))[1:])

print(group_list)

for group in group_list:
    for elem in range(0,len(group)):
        if Group_graph.get(group[elem])!=None:
            #todo then we add disjoints between initial group and the key list
            Group_graph[group[elem]].extend(findDisjoint(group[elem],group,Group_graph[group[elem]]))
        else:
            #todo add the remaining elemnt in group to the list of elemnt
            Group_graph[group[elem]]=findDisjoint(group[elem],group,[])

print(Group_graph)
stacklist=[]
for i in range(1,a+1):
    if Group_graph.get(i)!=None:
        print(getConnection(i))
    else:
        print(1,end="")


