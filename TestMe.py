test_case=int(input())
j=0

traverse=dict()

def Pathfind(matrix,initil_vec,final_vec,distance):
    distance+=1
    flag=False
    if matrix[initil_vec[0]][initil_vec[1]][0]==1:
        return False,-1
    elif initil_vec==(final_vec):
        return True,distance
    elif matrix[initil_vec[0]][initil_vec[1]][1]==0:
        return False,-1
    else:
        manhatan=matrix[initil_vec[0]][initil_vec[1]][1]
        tmp=[]
        small=500
        for i in range(-manhatan,manhatan+1):
            for j in range(-manhatan,manhatan+1):
                if i+j==manhatan:
                    if i>=0 and j>=0 and matrix[initil_vec[0]][initil_vec[1]][0]==0:
                        tmp=Pathfind(matrix,(i,j),final_vec,distance);
                    if tmp[0]:
                        flag=True
                        if small>tmp:
                            small=tmp
                    
        #this node is treversed
        matrix[initil_vec[0]][initil_vec[1]][0]=1
        return True,small

while j!=test_case:
    j+=1
    row,col=[int(i) for i in input().split(" ")]
    print(row)
    mat=[]
    tmp=[]
    for i in range(0,row):
        tmp=list(zip([0]*col,list(map(int,input().split(" ")))))
        mat.append(tmp)
    sx,sy=list(map(int,input().split(" ")))
    sx-=1
    sy-=1

    Query=int(input())
    querytup=tuple()
    for i in range(0,Query):
        querytup=tuple([int(x)-1 for x in input().split(" ")])
        print(Pathfind(mat,(sx,sy),querytup,1))


