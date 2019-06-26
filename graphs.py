import queue

def dfs(graph,index,visit=None):
    if visit==None:
        visit={index:1}
    if graph.get(index)==None:
        print(index)
        return
    else:
        print(index)
        for elem in graph[index]:
            if visit.get(elem)==None:
                visit[elem]=1
                dfs(graph,elem,visit)
        graph
    pass
def bfs(graph):
    traverse=dict()
    first_elem=list(graph.keys())[0]
    BFSQueue=queue.Queue()
    traverse[first_elem]=1
    BFSQueue.put([first_elem,0])
    level=0
    while(not BFSQueue.empty()):
        vertex,level=BFSQueue.get()
        print(vertex,level)
        if graph.get(vertex)!=None:
            for elem in graph[vertex]:
                if traverse.get(elem)==None:
                    traverse[elem]=1
                    BFSQueue.put([elem,level+1])





if __name__=="__main__":
    graph={1 :[2,3,4],2:[5,6],3:[7,8],4:[9,10],9:[13,45],13:[22,34,12]}
    bfs(graph)
    dfs(graph,list(graph.keys())[0])


