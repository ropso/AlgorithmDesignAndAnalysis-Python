import copy
class TestClass:
    '''TestClass checking how copying of item works
    '''
    def __init__(self,num):
        self._num=copy.deepcopy(num)

    def print_num(self):
        print(self._num)

if __name__ =="__main__":
    num1=[21]
    a=TestClass(num1)
    num1.append(23)
    a.print_num()
    print(num1)

