tot_inp=int(input())
while(tot_inp>0):
    tot_inp-=1
    num=int(input())

    inp_list=list(map(int,input().split(" ")))
    modified_list1=[]
    modified_list2=[]
    if len(inp_list)==1:
        if inp_list[0]==1:
            print('Yes')
        else:
            print("No")
    else:
        for i in range(0,len(inp_list)):
            if inp_list[i]==1:
                modified_list1=inp_list[i:]+inp_list[:i]
                modified_list2=inp_list[:i]+inp_list[i:]
        flag1=True
        for i in range(0,len(modified_list1)):
            if modified_list1[i] != i+1:
                flag1=False
                break
        flag2=True
        for i in range(0,len(modified_list2)):
            if modified_list2[i] != i+1:
                flag2=False
                break
        print(modified_list1,modified_list2)
        if flag1 or flag2:
            print('Yes')
        else:
            print('No')

