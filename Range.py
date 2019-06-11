class Range:
    def __init__(self,start,stop=None,step=1):
        if step==0:
            raise ValueError("step cant be zero")
        elif stop==None:
            start,stop=0,start
        self._length=max(0,(stop-start+step-1)//step)
        self._start=start
        self._step=step
    def __len__(self):
        return self._length
    def __getitem__(self,k):
        if k<0:
            k+=len(self)
        if not 0<=k< self._length:
            raise IndexError('Index Out Of range')
        return self._start+k*self._step

if __name__=="__main__":
    for i in Range(0,23,3):
        print(i)
    for j in Range(90):
        print("the red hood ",j)


