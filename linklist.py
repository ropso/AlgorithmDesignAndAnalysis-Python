class LinkedList:

    class _Node:
        __slots__='_value','_next'
        def __init__(self,value=None,next_node=None):
            self._value=value
            self._next=next_node



    def __init__(self):
        self._head=None
    def insert(self,value):
        if self._head==None:
            self._head=self._Node(value)
        else:
            index=self._head
            while(index._next!=None):
                index=index._next
            index._next=self._Node(value)

    def printList(self):
        index=self._head
        while(index!=None and index._value!=None):
            print(index._value)
            index=index._next
    # delete the middle elements
    def removeDuplicate(self):
        index=self._Node("1")
        index._next=self._head
        elem_dict={}
        while(index._next!=None):
            print("##",index._value)
            """index=index._next"""
            if elem_dict.get(index_value)==None:
                elem_dict[index._next._value]=1
                print(elem_dict)
            else:
                index._next=index._next._next
                print("#",index._next._value)
                    
            index=index._next
            
                # remove t  his entry put the index=index._next

    def RemoveDuplicateCleaner(self):
        index=self._head
        previous=self._Node()
        elem_dict={}
        while(index!=None):
            if elem_dict.get(index._value)==None:
                elem_dict[index._value]=1
                previous=index
            else:
                previous._next=index._next
                index=previous
            index=index._next
if __name__=="__main__":
    ls=LinkedList()
    
    ls.insert(89)
    ls.insert(89)
    ls.insert(78)
    ls.insert(891)
    ls.insert(78)
    ls.insert(9)
    ls.insert(78)
    ls.insert(8)
    ls.insert(8)
    ls.printList()
    ls.RemoveDuplicateCleaner()
    print("%")
    ls.printList()
    #ls.deleteElement(2)