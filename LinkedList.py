class LinkedStack:
    '''lifo implementation using singliy linked list'''
    class _Node:

        """lightweight node object"""
        __slots__='_element','_next'
        def __init__(self,element,next):
            self._element=element
            self._next=next
    def __init__(self):
        """create an empty stack"""
        self._head=None
        self._size=0
    def push(self,elem):
        self._head=self._Node(elem)
