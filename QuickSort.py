
def partion(partlist,low,high):
    firsthigh=low
    piviot=high
    for i in range(low,high):
        if partlist[i]<partlist[piviot]:
            partlist[i],partlist[firsthigh]=partlist[firsthigh],partlist[i]
            firsthigh=firsthigh+1
    partlist[piviot],partlist[firsthigh]=partlist[firsthigh],partlist[piviot]
    return firsthigh    

def QuickSortme(s,l,h):
    if(h-l>0):
        p = partion(s,l,h)
        QuickSortme(s,l,p-1)
        QuickSortme(s,p+1,h)
io=[23,32,43,67,45,34,33,65,90,13,42,56,456,78]

QuickSortme(io,0,len(io)-1)
print(io)