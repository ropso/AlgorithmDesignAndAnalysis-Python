def multiply(num1,num2):
    if num1<10 and num2<10:
        return num1*num2
    else:
        num_length=len(str(num1)) if len(str(num1)) >len(str(num2)) else len(str(num2))
        num1_length=len(str(num1))
        num2_length=len(str(num2))
        num1_partition=num_length//2
        num2_partition=num_length//2
        
        a=num1//(10**num1_partition)
        b=num1%(10**num1_partition)
        c=num2//(10**num2_partition)
        d=num2%(10**num2_partition)
        #print(a,b,c,d)
        # we have to find -> ac* 10^(Na+Nb)/2 +  bd  +  
        #  ad
        firstcoeff=multiply(a,c)
        third_coef=multiply(b,d)
        second_coef=multiply(a+b,c+d)-firstcoeff-third_coef
   
        return 10**num1_length*firstcoeff+10**num1_partition*(second_coef)+third_coef

def karat(x,y):
    if len(str(x))== 1 or len(str(y))==1:
        return x*y

    n = max(len(str(x)),len(str(y))) // 2

    a = x // 10**(n)
    b = x % 10**(n)
    c = y // 10**(n)
    d = y % 10**(n)

    z0 = karat(b,d)
    z1 = karat((a+b), (c+d))
    z2 = karat(a,c)

    return ((10**(2*n))*z2)+((10**n)*(z1-z2-z0))+z0
if __name__=="__main__":
    print(karat(3141592653589793238462643383279502884197169399375105820974944592

,2718281828459045235360287471352662497757247093699959574966967627))
        # we have to find ac bd and bd+dc