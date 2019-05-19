mat=[[51,32,33,41,],[37,14,55,60],[79,84,39,10],[34,54,12,43]]
for i in mat:
    for j in i:
        print j,
    print
for i in range(0,len(mat[0])): 
    for j in range(len(mat)-1,-1,-1):
        print mat[j][i],
    print
def rotatelo(mat):
    mat2=[]
    tmp=[]
    for i in range(0,len(mat[0])): 
        for j in range(len(mat)-1,-1,-1):
            tmp.append(j)
            print(mat[j])
        mat2.append(tmp)
        tmp=[]
    return mat2

print(rotatelo([[3, 1],[4, 2]]))