class Derivatives:
    '''Derivtive class: generate nth order derivative of polynomial'''
    def __init__(self,polynomial):
        '''constructor need 1 args string form polynomial var notaio must be using x 
        example 23x^200+x**12'''
        self._polynomial=[]
        if isinstance(polynomial,(str)):
            value=polynomial.split("+")
            self._polynomial=[i.split("x^") for i in value]
    def show(self):
        print(self._polynomial)
    def nth_derviate(self,n):
        #todo
        derivate=sorted(self._polynomial,key=lambda x: x[1])
        i=0
        for elem in derivate:
            elem[1]=int(elem[1])
            elem[0]=int(elem[0])
        counter=n
        #print(derivate)
        while i<len(derivate) and derivate[i][1]>=n:
            while counter!=0:
                #print(i,counter)
                if derivate[i][1]==0:
                    break
                derivate[i][0]=derivate[i][0]*derivate[i][1]
                derivate[i][1]-=1
                counter-=1
            counter=n
            i+=1
        li=[]
        derivative_poly=sorted(derivate,key=lambda x : x[1],reverse=True)
        for elem in derivative_poly:
            li.append(str(elem[0])+"x^"+str(elem[1]))
        print("+".join(li))
if __name__=="__main__":
    poly_test=input()
    derivate=Derivatives(poly_test)
    #derivate.show()
    derivate.nth_derviate(2)
