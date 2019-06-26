import queue

def addToEvenOddSet(even_set,odd_set,graph): 
    i=0
    traverse_nex_que=queue.Queue(10**5+1)
    traverse_nex_que.put([list(graph.keys())[0],i])
    
    while (len(odd_set)<=(len(graph)//2) and len(even_set))<=(len(graph)//2):
        if not traverse_nex_que.empty():
            elem=traverse_nex_que.get()
        else:
            #print(len(traverse_nex_que))
            break
        #print(elem,end="*",)
        if elem[0] not in odd_set and elem[0] not in even_set  :
            if elem[1]%2==0:
                even_set.add(elem[0])
            else:
                odd_set.add(elem[0])
        if graph.get(elem[0])==None:
            continue
        for vertex in graph[elem[0]]:
            traverse_nex_que.put([vertex,elem[1]+1])
    #print(graph)    
    select_set=odd_set if len(odd_set)<len(even_set) else even_set
    print(len(select_set))
    for elem in select_set:
        print(elem,end=" ")
    print()
    




tot_test=int(input())

while(tot_test>0):
    tot_test-=1
    n,m=[int(i) for i in input().split(" ")]
    adjancey_mat={}
    oddset=set()
    evenset=set()
    for i in range(0,m):
        vertex,conect_to=(int(i) for i in input().split(" "))
        if adjancey_mat.get(vertex)!=None:
            adjancey_mat[vertex].append(conect_to)
        else:
            adjancey_mat[vertex]=[conect_to]
    addToEvenOddSet(evenset,oddset,adjancey_mat)

    #print(adjancey_mat)

# very unoptimised codes 