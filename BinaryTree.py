class Node:

    def __init__(self,key):
        self.left=None
        self.right=None
        self.key=key
        self.extremness=0

    def __str__(self):
        return(str("the key is "+str(self.key)+" "+str(self.right)+" "+str(self.left)))
root=Node(23)
root.right=None
root.left=None
root.extremness=0
vrt_line=dict()
for i in range(-7,8):
    vrt_line[i]=[]

vrt_line[0].append(23)

root.extremness=0
print(root)
def AddNode(num):
    # first find the right positions and then insert
    tmp=root
    extreme=0
    while(tmp!=None):
        if tmp.key>=num:
            if tmp.left==None:
                tmp.left=Node(num)
                tmp.left.left=None
                extreme-=1
                tmp.left.extremness=extreme
                tmp.left.right=None
                print(extreme)
                print("printing in left",tmp.left)
                vrt_line[extreme].append(tmp.left.key)
                break
            else:
                tmp=tmp.left;
                extreme-=1
        elif tmp.key<=num:
            if tmp.right==None:
                tmp.right=Node(num)
                tmp.right.right=None
                extreme+=1
                tmp.right.extremness=extreme
                tmp.right.left=None
                print(extreme)
                print("printing on right",tmp.right)
                vrt_line[extreme].append(tmp.right.key)
                break
            else:
                tmp=tmp.right
                extreme+=1


def Showtree(node):
    if node==None:
        return 
    else:
        Showtree(node.left)
        print(node.key,"extemness is",node.extremness)
        Showtree(node.right)

AddNode(34)
AddNode(56)
AddNode(4)
AddNode(89)
AddNode(390)
AddNode(1)
AddNode(26)

Showtree(root)


print("the verical travers is ")
for  elem in vrt_line:
    print("the vertical line",elem,"and the key elemnt is",vrt_line[elem])