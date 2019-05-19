equation_string=input()
equation_string2=equation_string
for i in range(0,len(equation_string2)):
    if equation_string[i]=="*":
        num1=int(equation_string[i-1])*int(equation_string[i+1])
        equation_string2=equation_string[:i-1]+str(num1)+equation_string[i+1:]
print(equation_string)