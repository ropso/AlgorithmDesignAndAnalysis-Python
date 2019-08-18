def algoPeration(num_series,num_at_indx):
    num_series.insert(0,0)
    i=1
    while(i<len(num_series)):
        num_series.pop(i)
        i+=1
        #print(num_series)
    
    return num_series[num_at_indx]




if __name__=="__main__":
    # todo unit testing
    test_num=3
    wndr_num_tst=1
    print(algoPeration(list(range(1,test_num+1)),wndr_num_tst))
