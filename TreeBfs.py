class Tree:
    class _Node:
        def __init__(self,value,right,left):
            self._value=value
            self._right=right
            self._left=left

    def __init__(self):
        self._root_node=None

