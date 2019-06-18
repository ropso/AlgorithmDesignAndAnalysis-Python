class Vector:
    '''Vector class modeling Vectors'''
    def __init__(self,initialise_param):
        '''constructor:-create list of num length'''
        if isinstance(initialise_param,(Vector,list)):
            self._coords=[i for i in initialise_param]
        
        elif isinstance(initialise_param,(int)):
            if initialise_param<=0:
                raise ValueError("bhai mat kar bhai mat kar chutiye")
            
            else:
                self._coords=[0]*initialise_param

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
    def __sub__(self,vec):
        if len(self)!=len(vec):
            raise ValueError("both must have same dimension")
            return
        subtracted_vec=Vector(len(self))
        for i in range(0,len(vec)):
            subtracted_vec[i]=self[i]-vec[i]
        return subtracted_vec
    def __neg__(self):
        neg_vector=Vector(len(self))
        for i in range(0,len(self)):
            neg_vector[i]=-1*self[i]
        return neg_vector

    # adding functionality to add list+vector return vector
    def __mul__(self,multby_vec):
        num=multby_vec
        if isinstance(num,(int,float)):
            vec=Vector(len(self))
            for i in range(0,len(self)):
                vec[i]=num*(self[i])
            return vec
        elif isinstance(multby_vec,list):
            if len(self)!=len(multby_vec):
                raise ValueError("must be of same length")
            else:
                dot_product=0
                for i in  range(0,len(multby_vec)):
                    dot_product+=multby_vec[i]*self[i]
                return dot_product
            
                    



    def __radd__(self,add_list):
        if len(self)!= len(add_list):
            raise ValueError("must be of same length for valid operation")
        new_vec=Vector(len(self))
        for i in range(0,len(self)):
            new_vec[i]=self[i]+add_list[i]
        return new_vec

if __name__ == "__main__":
    v1=Vector(3)
    v2=Vector(3)
    v1[2]=1
    v2[1]=34
    v3=v1+v2

    print(v3)
    v4=v3-v1
    print("v3 is",v3,"\n v1 is \n",v1,"so the result after subtartion is ",v4)
    print("after negating the values",-v4)

    ##ading list to vector adding functionality 
    v5=[1,2,3]+v4
    print('adding lit to the elements []1,2,3]',v5)
    ## adding test of multiply operators
    v6=v5*[1,2,3]# act  as a dot product 
    print('multipled vector is',v6)
    v6=v5*2
    print(v6)
    #v6=2*v5
    print(v6)
    # adding test for overriden Counstructors
    new_vec=Vector([34,12,344,5])

    print(new_vec)