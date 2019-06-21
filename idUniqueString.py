def isUnique(test_str):
    test_str=list(test_str) 
    test_str.sort()
    for i in range(0,len(test_str)-1):
        if test_str[i]==test_str[i+1]:
            return False
    return True
    #complexity is o(n)

def isUniqueBitVector(test_str):
    if(len(test_str)>126):
        return False
    '''suppose we are considering that 26 caharacter are allowed in shtroi'''
    #we can make that kind of hasing too ut we didint whnt to 
    test_str_list=list(test_str)
    test_str_words_dict={}
    #for optimisation we are going to use bit vector 
    #and remove the workin of dictionary
    elem_occurance=0
    for elem in test_str_list:
        index=(ord(elem)-ord('a'))
        if (elem_occurance&(1<<index))>0:
            return False
        else:
            elem_occurance|=(1<index)
    return True
    #code complexity o(n) and 




if __name__=="__main__":
    test_string1="kuldeepparashar"
    test_string2="ajioklm"
    print("test_case1",isUnique(test_string1))
    print("testcase2",isUnique(test_string2))
    print("test_case1",isUniqueBitVector(test_string1))
    print("testcase2",isUniqueBitVector(test_string2))


