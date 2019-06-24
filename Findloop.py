class Linklist:
    class _Node:
        __slots__="_next","_value"
        
        def __init__(self,value,next):
            self._next=next
            self._value=value

    def __init__(self,):
        self._head=None
    def insert(self,value):
        if self._head==None:
            self._head=self._Node(value)
        else:
            index=self._head
            while(index._next!=None):
                index=index._next
            index._next=
