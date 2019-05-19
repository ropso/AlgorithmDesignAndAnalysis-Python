row,col=map(int,input().split())
if row!=1 or col!=1:
    mat1=[]
    flag=True
    for i in range(0,row):
        li=[]
        tmp=input()
        tmp=tmp.split(" ")
        li=list(map(int,tmp))
        mat1.append(li)
    mat2=[]
    for i in range(0,row):
        li=[]
        tmp=input()
        tmp=tmp.split(" ")
        li=list(map(int,tmp))
        mat2.append(li)
    for i in range(0,row-1):
        for j in range(0,col-1):
            if mat1[i][j]>=mat1[i+1][j] or mat2[i][j]>=mat2[i][j+1] or mat1[i][j]>=mat1[i][j+1] or mat2[i][j]>=mat2[i+1][j]:
                mat1[i][j],mat2[i][j]=mat2[i][j],mat1[i][j]
                if not(mat1[i][j]<mat1[i+1][j] and mat2[i][j]<mat2[i][j+1] and mat1[i][j]<mat1[i][j+1] and mat2[i][j]<mat2[i+1][j]):
                    flag=False
                    break
    if flag:
        print('Possible')
    else:
        print("Impossible")
else:
    flag=True
    if row==1:
        collist1=list(map(int,input().split(" ")))
        collist2=list(map(int,input().split(" ")))
        for i in range(0,col-1):
            if collist1[i]>collist1[i] or collist2[i]>collist2[i]:
                collist1[i],collist2[i]=collist2[i],collist1[i]
                if collist1[i]>=collist1[i] or collist2[i]>=collist2[i]:
                    flag=False
                    break
        if flag:
            print("Possible")
        else:
            print('Impossible')
    elif col==1:
        rowlist1=[]
        rowlist2=[]
        for i in range(0,row):
            rowlist1.append(int(input()))
        for j in range(0,row):
            rowlist2.append(int(input()))
        
        for i in range(0,row-1):
            if rowlist1[i]>rowlist1[i] or rowlist2[i]>rowlist2[i]:
                rowlist1[i],rowlist2[i]=rowlist2[i],rowlist1[i]
                if rowlist1[i]>=rowlist1[i] or rowlist2[i]>=rowlist2[i]:
                    flag=False
                    break
        if flag:
            print("Possible")
        else:
            print('Impossible')
    elif col==1 and row ==1:
        print("possible")
    
