import copy

string1="kuldeep"
list1=list("kuldeep")
list3=copy.copy(list1)

list3.append("sdasdasd")
print("the main list is ",list1)
print("this is list three",list3)
list2=list1
list2.append("sdfs")

string2=string1
num1=90
num2=num1
num2=num2+12
print(num1)
print(num2)
num2+=1
print(num1)
print(num2)
string2+=string1
print(string1)
print(string2)
print(list1)
print(list2)

