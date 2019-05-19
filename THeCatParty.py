"""
1:find the power on recurence A^n
2:to following procedure for (n,delPower=1) and n-1 and setting delePower=0
    A:interatate over each elemnt in array with window size of n till any mismatch happen
    B:if not match then stop from return first index of non match window instance
    C: return the index
4: choose MAx index from both

#Edge cases
A^nB^n need to be handled appropriately
A^nB^nC^n~~~N^N must return first index of last window

# input 
non Caps Alphabatical string
output:
mXINDEX WHERE LEAFT OUT ARE ALLL STRE

"""
def strict_check():# when delpow lost
    pass
def loose_check():# when del pow is there
    pass
opcode=input()# input
def getFirstIndex(pattern,delpow):
    if len(pattern)>3:
        if pattern[0]!=pattern[1]:
            if pattern[1]!=pattern[2] and pattern[2]!=pattern[0]:
        #can be a case of abbbb abbdbb must be canceled        
    else:
        return 3

