import linklist as lk1

class linklist(lk1):
    def __init__(self):
        super().__init__()
    
    def KthFromLast(self,indexk,node=12):
        if node==12:
            node=self._head
        if node==None:
            return [0,node]
        else:
            tmp=KthFromLast(indexk,node._next)
            if tmp[0]+1==indexk:
                return [indexk,node]
            else:
                return [tmp[0]+1,node]
        
if __name__=="__main__":
    a=linklist()
    a.insert(23)
    a.insert(34)
    a.insert(23)
    a.insert(45)
    a.insert(565)
    a.insert(43)
    print(a.KthFromLast(3))