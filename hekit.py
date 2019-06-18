test_casecounter=int(input())

while test_casecounter>0:
    #print(test_casecounter)
    test_casecounter-=1
    num=input()
    aray=list(map(int,input().split(" ")))
    elem_sum=0
    max_elem=aray[0]
    for elem in aray:
        if elem >max_elem:
            max_elem=elem
        elem_sum+=elem
    if (elem_sum-max_elem) >max_elem:
        print('YES')
    else:
        print('NO')