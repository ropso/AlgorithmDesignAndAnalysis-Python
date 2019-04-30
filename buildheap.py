class Binheap:
    def __init__(self, *args, **kwargs):
        self.heaplist=[0]
        self.currentSize=0
    def insert(self,k):
        self.heaplist.append(k)
        self.currentSize=self.currentSize+1
        self.percUp(self.currentSize)

    def percUp(self,i):
        while i//2>0:
            if self.heaplist[i]>self.heaplist[i//2]:
                tmp=self.heaplist[i//2]
                self.heaplist[i//2]=self.heaplist[i]
                self.heaplist[i]=tmp
            i=i//2
    def show(self):
        for i in self.heaplist:
            print(i)



Binheapp= Binheap()
Binheapp.insert(2)
Binheapp.insert(34)
Binheapp.insert(12)
Binheapp.insert(33)
Binheapp.insert(123)
Binheapp.insert(3)
Binheapp.show()
