from math import sqrt
def IsPrimeNo(no):
    if no <=1:
        return False
    for i in range(2,(int(sqrt(no))+1)):
        if no%i==0:
            return False
    return True

def IsPrimeVariant(no):
    #we would check utp the exact squareroot
    if no <=1:
        return False
    i=2
    while i*i<=no:
        if no%2==0:
            return False
        i+=1
    return True

if __name__=="__main__":
    #Test Case 1 no=12 prime no
    print(" a prime" if IsPrimeNo(12) else  "Not a prime")
    print(" a prime" if IsPrimeVariant(12) else  "Not a prime")
    #Test case 2 no=23 prime no
    print("Is a prime" if IsPrimeNo(23) else  "Not a prime")
    print("Is a prime" if IsPrimeVariant(23) else  "Not a prime")
    #Test Case 3 np =-12 
    print(" a prime" if IsPrimeNo(-12) else  "Not a prime")
    print(" a prime" if IsPrimeVariant(-12) else  "Not a prime")
    #TestCase 4 no=1
    print("Is prime" if IsPrimeNo(1) else "Not a Prime")



    