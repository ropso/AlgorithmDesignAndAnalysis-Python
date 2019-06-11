class ComplexNo:
    '''class to store anad perform opeation on complex no'''
    def __init__(self,imaginarynum,realnum):
        self._imaginarynum=imaginarynum
        self._realnum=realnum
    
    def getImaginary(self):
        return self._imaginarynum;
    
    def getReal(self):
        return self._realnum

    def __add__(self,obj):
        temp_imaginary=self._imaginarynum+obj.getImaginary()
        temp_real=self.getReal()+self._realnum
        tmpObj=ComplexNo(temp_imaginary,temp_real)
        return ComplexNo(temp_imaginary,temp_real)

if __name__=="__main__":
    cn1=ComplexNo(2,3)
    cn2=ComplexNo(3,4)
    cn3=cn1+cn2# here we have done operator overlaodin on the Complex object 
    
    print(cn3.getImaginary())