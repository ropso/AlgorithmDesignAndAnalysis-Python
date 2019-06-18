def getGcd(num1,num2):
    if num1>num2:
        num2,num1=num1,num2
    if num2%num1==0:
        return num1
    tmp=0
    while num2>0:
        num1=num1%num2
        num1,num2=num2,num1
    return num2
def zippedarrange(item_list):
    item_list.sort()
    for index in range(0,len(item_list)//2):
        print(item_list[len(item_list)-1-index],end=" ")
        print(item_list[index],end=" ")

if __name__=="__main__":
    print(getGcd(5,36))

    zippedarrange([23,56,34,90,78,65,45,59,67,10])

