
def rotate_eve_odd(rotate_str,num):
    if num%2==0:
        num=num*2
        return rotate_str[num:]+rotate_str[:num]
    else:
        return rotate_str[num:]+rotate_str[:num]

if __name__=="__main__": 
    test_string="Kuldeep parashar"    
    print(rotate_eve_odd(test_string,4))
    