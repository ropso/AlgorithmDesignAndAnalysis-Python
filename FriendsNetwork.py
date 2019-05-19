def arrange(A):
    N=len(A)
    for i in range(0,N):
        print("@@@@@@@@@",A[i],A[A[i]],i)
        A[i]=A[i]+((A[A[i]]%N)*N)
        print(A[i])
        A[i]=A[i]//N
        print(A[i],"@@@@@@@@@@@@")
    return A 

print(arrange([ 4, 0, 2, 1, 3 ]))