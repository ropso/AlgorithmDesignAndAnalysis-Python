no_of_test_case=int(input())
noLength=11
flag=False
while no_of_test_case!=0:
    no_of_test_case-=1
    no_string=input()
    flag=False
    """we are trying to iteratre window length of 11 and if we find some thing stating with 8 we find a no
    """
    for i in range(0,(len(no_string)-(noLength-1))):
        if no_string[i] =='8':
            flag=True
            break
    if flag:
        print("No")
    else:
        print("Yes")


