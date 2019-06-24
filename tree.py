class NTree:
    '''by default its implemntation of binary search tree'''
    
    # making a inner class of nodes
    class node:
        __slots__="_value","_right","_left","_depth"
        def __init__(self,value,right,left,depth=0):
            self._right=right
            self._left=left
            self._value=value
            self._depth=depth
            

    def __init__(self,max_no_of_child=0):
        self._max_no_of_child=max_no_of_child
        self._root_node=None
    
    def insert(self, value):
        if self._root_node==None:
            self._root_node=self.node(value,None,None)
        else:
        # here we are going to insert as per binary tree rule 
        # 1>no node has more than 2 childs 
        # 2> lef_sb_tree<root<rightsub_tree
            runner=self._root_node
            while(runner!=None):
                if runner._value>value:
                    if runner._left==None:
                        runner._left=self.node(value,None,None)
                        break
                    else:
                        runner=runner._left
                    
                elif runner._value<=value:
                    if runner._right==None:
                        runner._right=self.node(value,None,None)
                        break
                    else:
                        runner=runner._right
                
    def InOrderTree(self,node):
        if node==None:
            return 
        else:
            self.InOrderTree(node._left)
            print(node._value)# in inorder trevarsal would give us sorted ist
            self.InOrderTree(node._right)

    def findMinInTree(self,node,counter=-1):
        counter+=1
        if node._left==None:
            return [node._value,counter]
        else:
            return self.findMinInTree(node._left,counter)

    def findMaxElemInTree(self,node,counter=-1):
        pass

if __name__=="__main__":
    tree=NTree()
    tree.insert(23)
    tree.insert(89)
    tree.insert(11)
    tree.insert(78)
    tree.insert(1)
    tree.InOrderTree(tree._root_node)

    print("the min value in the tree is ",tree.findMinInTree(tree._root_node))