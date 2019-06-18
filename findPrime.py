import math
prime_dict=dict()


def is_prime(n):
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True

if __name__=="__main__":
    num=int(input())
    i=2
    while i <=num:
        if is_prime(i):
            print(i,end=" ")
        i=i+1
