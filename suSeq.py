num1=24+1#11000

def isBitSet(num,indexFromLeft):
    mask=2**indexFromLeft
    return True if num&mask==mask else False # using addoerator 

def flipBit(num,indexFromLeft):
    if isBitSet(num,indexFromLeft):
        num=num-(2**indexFromLeft)
    else:
        num+=(2**indexFromLeft)
    return num
print("is bit no 4 is set from left in in num 24",isBitSet(num1,4))

print('the num flip ',"{0:b}".format(num1),bin(num1),"{0:b}".format(flipBit(num1,4)))