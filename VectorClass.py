class Vector:
    '''Vector class modeling Vectors'''
    def __init__(self,num):
        '''constructor:-create list of num length'''
        self._coords=[0]*num
    def __len__(self):
        return len(self._coords)
    def __getitem__(self,j):
        return self._coords[j]
    def __setitem__(self,at_index,val):
        self._coords[at_index]=val
    def __add__(self,vector):
        if len(self)!=len(vector):
            raise ValueError("dimension  of the vector must be same")
        result=Vector(len(self))
        for j in range(0,len(self)):
            print(j)
            print(self[j],vector[j])
            result[j]=self[j]+vector[j]
        return result
    def __eq__(self,vector):
        return True if vector == self else False
    
    def __ne__(self,vector):
        return not self==vector
    
    def __str__(self):
        return "<"+str(self._coords)[1:-1]+">"

if __name__ == "__main__":
    v1=Vector(3)
    v2=Vector(3)
    v1[2]=1
    v2[1]=34
    v3=v1+v2
    print(v3,help(v3))