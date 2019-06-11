def FindPairsSpaceN(list_a,dif):
    a_element=dict()
    pair_list=[]
    for elem in list_a:
        a_element[elem]=1
    for elem in list_a:
        if a_element.get(elem+dif) != None:
            pair_list.append((elem,elem+dif))
        if a_element.get(elem-dif)!=None:
            pair_list.append((elem,elem-dif))
    return pair_list


if __name__=="__main__":
    test_list=[1,4,8,6,3,9,7,2,5,10]
    print(FindPairsSpaceN(test_list,3))

