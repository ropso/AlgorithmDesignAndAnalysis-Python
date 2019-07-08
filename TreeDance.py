class Tree:
    class _node:
        __slots__="_value","_right_node","_left_node"
        def __init__(self,value):
            self._value=value
            self._right_node=None
            self._left_node=None
    def __init__(self):
        self._root_node=None
        self._tot_elem=None
    def insert(self,value):
        if self._root_node==None:
            self._root_node=self._node(value)
        else:
            traverse=self._root_node
            while(traverse!=None):
                if value>traverse._value:
                    if traverse._right_node!=None:
                        traverse=traverse._right_node
                    else:
                        traverse=
