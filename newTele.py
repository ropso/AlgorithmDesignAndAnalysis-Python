import copy
no_of_test_case=int(input())
noLength=11
while no_of_test_case!=0:
    input()   
    no_string=input()
    #print(no_string,no_of_test_case)
    no_of_test_case-=1
    if len(no_string)<11:
        print('No')
        continue
    elif len(no_string)==11:
        if no_string[0]=="8":
            print("Yes")
        else:
            print("No")
        continue
    else:

        #print(no_string,"\n&&&&&&&&&&&&&&&&&&&&&&&&")
        flag=False
        no_string=list(no_string)
        no_string=list(map(int,no_string))
        No_copy=copy.copy(no_string)
        no_string.sort(reverse=True)
        i=0
        no_index=dict()
        for j in range(0,10):
            no_index[j]=0
        while no_string[i]>=7 and i <len(no_string)-1:
            no_index[no_string[i]]+=1
            i+=1
        #print(no_string,'the dixtionary is',no_index)
        # now check that last how much 8 is in last 10 biths
        end_string=No_copy[-10:]
        lasteight=0
        for elem in end_string:
            if elem==8:
                lasteight+=1
        if no_index[8]>lasteight:
            print('Yes')
        else:
            print('No')
    




