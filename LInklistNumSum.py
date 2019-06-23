def NumSumReverse(ar1,ar2):
    # suppose we are getting int arraay of num
    ar3=[]
    str1_len,str2_len=len(ar1),len(ar2)
    tot_iteration=max(str1_len,str2_len)
    addpadding(ar1 if str1_len<str2_len else ar2,abs(str1_len-str2_len),after=True)
    carray=0
    print(len(ar1),len(ar2))
    for i in range(0,tot_iteration):
        sum=ar1[i]+ar2[i]+carray
        carray=sum//10
        ar3.append(sum%10)
    if carray>0:
        ar3.append(carray)
    return ar3

def addpadding(arr,num,before=False,after=False):
    if before and after:
        
        raise ValueError("both before and after cant be simultaneously on")
    elif after:
        print(arr)
        for i in range(0,num):
            arr.append(0)
        print(arr)


if __name__=="__main__":
    #Test1:-
    ar1=[9,8,1,4,2]
    ar2=[2,3,5,1,1,2,2]
    ar3=NumSumReverse(ar1,ar2)
    print(ar3)