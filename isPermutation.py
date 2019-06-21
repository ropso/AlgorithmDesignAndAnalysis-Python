def isPermutation1(str1,str2):
    if len(str1)!=len(str2):
        return False
    else:
        str1_word_frequency=dict()
        str2_word_frequency=dict()
        for i in range(0,len(str1)):
            str1_word_frequency[str1[i]]
    pass
    
def isPermuataion2(str1,str2):
    #time complexity of algorithm bigo(n*lg(n))
    if len(str1)!=len(str2):
        return False
    str1=list(str1)
    str2=list(str2)
    str1.sort()
    str2.sort()
    for i in range(0,len(str1)):
        if str1[i]!=str2[i]:
            return False
    return True


if __name__=="__main__":
    print("test case 1: 'qwewqe','ewqwqe' is permutaion",isPermuataion2("qwewqe","ewqwqe"))