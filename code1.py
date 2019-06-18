if  __name__=="__main__":
    input_str=list(map(int,input().split(" ")))
    inp_array=input_str[2:]
    search_no=input_str[1]
    no_frq=dict()
    for elem in inp_array:
        if no_frq.get(elem)!= None:
            no_frq[elem]+=1
        else:
            no_frq[elem]=1
    print(no_frq[search_no])

