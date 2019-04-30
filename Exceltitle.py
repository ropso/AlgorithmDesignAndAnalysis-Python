def getExceltitle(n):
    max=50
    excelColName=list();
    i=0
    while(n>0):
        rmdr=n%26
        if rmdr==0:
            excelColName.append("Z")
            i+=1
            n=(n//26)-1
        else:
            excelColName.append(chr((rmdr - 1) + ord('A')))
            i=i+1
            n=n//26
        
    return "".join(reversed(excelColName))
print(getExceltitle(34))
