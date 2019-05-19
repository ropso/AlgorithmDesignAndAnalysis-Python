noOfCat,catLeft=input().split(" ")
noOfCat=int(noOfCat)
catLeft=int(catLeft)
noOfCat
priorityQue=[]
priorityQue.append(noOfCat-1)
catCounter=catLeft-1
if catLeft==0:
    print(1)
elif catLeft==1:
    print(1)
elif catLeft>=2:
    while catCounter>0:
        priorityQue.sort()
        try:
            tmp=priorityQue.pop()
        except:
            break
        grpsplit1=tmp//2
        grpsplit2=tmp-grpsplit1-1
        if grpsplit1>grpsplit2:
            if grpsplit2!=0 :
                priorityQue.append(grpsplit2)
            if grpsplit1!=0 :
                priorityQue.append(grpsplit1)
        else:
            if grpsplit1!=0 :
                priorityQue.append(grpsplit1)
            if grpsplit2!=0 :
                priorityQue.append(grpsplit2)
        catCounter-=1
    print(priorityQue.__len__())