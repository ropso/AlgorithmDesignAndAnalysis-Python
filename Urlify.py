def Urlify(urlifystring,str_length):
    # task 1 first find the total no of white spaces
    total_whitespace=0
    for i in range(0,str_length):
        if urlifystring[i]==" ":
            total_whitespace+=1
    #print(total_whitespace)
    url_length=str_length+total_whitespace*2
    url_index=url_length-1
    urlifystring=list(urlifystring)
    for i in range(str_length-1,-1,-1):
        if urlifystring[i]==" ":
            urlifystring[url_index]="0"
            url_index-=1
            urlifystring[url_index]="2"
            url_index-=1
            urlifystring[url_index]="%"
            url_index-=1
        else:
            urlifystring[url_index]=urlifystring[i]
            url_index-=1
    return "".join(urlifystring)



if __name__=="__main__":
    tstcase_str1="the kuldeep parashar      "# given extra space so that url can come in same list
    str_length=20
    print(Urlify(tstcase_str1,str_length))