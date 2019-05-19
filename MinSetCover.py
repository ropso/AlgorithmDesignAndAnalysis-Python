universalSet={23,32,12,45,56,67,7,89,80,96}
subSetList=[{23,32,12,45},{32,12,45,56},{56,67,7,89},{80,96},{12,45,56,67,7,89},{7,89,80,96},{89,80,96}]
def getMinSubSetList(universalSet,subSetList):
    SetDs=[[i,len(i)] for i in subSetList]
    tempSet=set()
    setList=[]
    while(len(universalSet)!=0):
        print("\n++++++++++++++++++++++++++++++++\n")
        SetDs=sorted(SetDs,key=lambda x :x[1])
        print("@@@@@@\n",SetDs,"\n@@@@@@@@@@@@|\n")
        tmpSet=SetDs.pop()[0]
        print(tmpSet)
        setList.append(tmpSet)
        tempSet=tempSet.union(tmpSet)
        print(tempSet)
        universalSet.difference_update(tempSet)
        SetDsi=SetDs
        SetDs=[]
        for elem in SetDsi:
            tmp=len(elem[0])-len(elem[0].intersection(tempSet))
            print("#############\n",elem[0],tempSet,elem[1],tmp,universalSet,"\n############")
            SetDs.append([elem[0],tmp])
        print("\n########DSI\n",SetDs,"\n########\n")
    return setList

print(getMinSubSetList(universalSet,subSetList))