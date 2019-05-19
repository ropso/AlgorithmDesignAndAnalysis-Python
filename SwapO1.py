def arrange(A):
        offset=len(A)+10
        print("the ofset ",offset)
        for i in range(0,len(A)):
            if A[i]<offset:
                tmp=A[i]
                A[i]=A[A[i]]
                print(A[i])
                A[i]=A[i]+offset
                try:
                    j=A.index(i)
                except ValueError:
                    continue
                if type(j)==type(3):
                    A[j]=tmp+offset
            print("\n************\n",A,"\n*****************\n")
            
        for i in range(0,len(A)):
            A[i]=A[i]-offset
        return A

print(arrange([ 4, 0, 2, 1, 3 ]))