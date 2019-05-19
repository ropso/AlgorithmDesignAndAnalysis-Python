toatl_stairs=int(input())
"""
we would use recursion to get different paterns which get upto final step when exactly get to end Add a global variables
"""
from unittest.case import skip
total_paths=0
Memo={}
""" complexity reduction using dynamic progrqming
 how?? like this try to memorize 
 """
def jumpChild(noStairsLeft):
    global total_paths
    global Memo
    try:
        return Memo[noStairsLeft]
    except:
        pass
    total_PathFromInstance=0
    if noStairsLeft<0:
        return 0
    elif noStairsLeft==0:
        total_paths=total_paths+1
        return 1
    else:
        total_PathFromInstance+=jumpChild((noStairsLeft-3))
        total_PathFromInstance+=jumpChild((noStairsLeft-2))
        total_PathFromInstance+=jumpChild((noStairsLeft-1))
        Memo[noStairsLeft]=total_PathFromInstance
        return total_PathFromInstance

print(jumpChild(toatl_stairs),Memo)
print(total_paths)

