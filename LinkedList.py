class LinkedStack:
    '''lifo implementation using singliy linked list'''
    class _Node:

        """lightweight node object"""


        __slots__='_element','_next'
        def __init__(self,element,next):
            self._element=element
            self._next=next
