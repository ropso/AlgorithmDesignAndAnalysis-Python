def Swap_array(ar):
    '''piviot the center elem and swap no from left sub art to right sub part'''
    array_length=len(ar)
    for i in range(0,array_length//2):
        ar[i],ar[array_length-i-1]=ar[array_length-i-1],ar[i]


if __name__=="__main__":
    # unit tests case 1 odd array
    test_aray=[23,1,23,4,54,67,3,23,12,211,43]
    Swap_array(test_aray)
    print(test_aray,len(test_aray))



    #usint test case 2 even array
    test_aray=[45,23,1,23,4,54,67,3,23,12,211,43]
    Swap_array(test_aray)
    print(test_aray)