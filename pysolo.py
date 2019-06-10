#for mutable then things += extend sthe object and operation wluld be reflected on the previouslly created 
#object no new ojec tis created

def SomeListHeck(test_list):
    ''' here we are going to add new elemnts 
    and want reflection back '''
    test_list+=[2,2,3,3]

def SomeListHeck2(test_list):
    '''here we didnt want to '''
    test_list=test_list+[34,12,45]

if __name__=="__main__":
    #todo est on videos
    testlist=[1,2,3,4,4]
    print(testlist)
    SomeListHeck(testlist)
    print(testlist)
    SomeListHeck2(testlist)
    print(testlist)
    test_string="i am a tester"
    test_string1=test_string
    test_string1+='dsjnd'
    print(test_string1)
