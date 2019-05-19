input()
test_string=input()
resultstring=[]
tot_del=0
for elem in  test_string:
    if len(resultstring)%2==0 and resultstring!="":
        resultstring.append(elem)
    elif len(resultstring)%2==1:
        if resultstring[-1]!=elem:
            resultstring.append(elem)
        else:
            tot_del+=1
            pass
#print(resultstring)
resultstring="".join(resultstring)
if len(resultstring)<=1:
    print(tot_del+1)
else:
    if len(resultstring)%2==0:
        print(tot_del,"\n",resultstring)
    else:
        print(tot_del+1);print(resultstring[:-1])