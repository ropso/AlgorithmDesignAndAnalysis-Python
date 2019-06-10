#python doesnot support method overloading we can use args an d krwgs

def Permutation(permuteString, prefix_string=""):

    if len(permuteString)==0:
        print(prefix_string)
    else:
        str_length=len(permuteString)
        if str_length==2:
            prefix_string1=prefix_string+permuteString[0]
            Permutation(permuteString[1],prefix_string1)
            prefix_string2=prefix_string+permuteString[1]
            Permutation(permuteString[0],prefix_string2)
        elif str_length==1:
            prefix_string3=prefix_string+permuteString[0]
            Permutation("",prefix_string3)
        else:
            for i in range(1,str_length-1):
                # print("isde loops",str_length,i)
                # print("#######",permuteString)
                # print(permuteString[0:i],permuteString[i+1:] ,prefix_string,permuteString[i])
                Permutation(permuteString[0:i]+permuteString[i+1:] ,prefix_string+permuteString[i])

            rem1=permuteString[1:]
            Permutation(rem1,prefix_string+permuteString[0])
            # print("isde loops",str_length,0)
            # print(rem1,prefix_string+permuteString[0])
                
            rem2=permuteString[0:str_length-1]
            Permutation(rem2,prefix_string+permuteString[str_length-1])
            #print("isde loops",str_length,str_length-1)
            #print(rem2,prefix_string+permuteString[str_length-1])
                

if __name__=="__main__":
    Permutation("abcd")