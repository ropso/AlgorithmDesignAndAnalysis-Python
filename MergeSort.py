def mergesort(Itemcontainer,leftindex,rightindex):
    if leftindex==rightindex:
        return 
    else:
        middle_index=(leftindex+rightindex)//2
        # left sub routine
        mergesort(Itemcontainer, leftindex, middle_index)
        # right sub routine
        mergesort(Itemcontainer, middle_index+1, rightindex)

        left_sorted_aray=Itemcontainer[leftindex:middle_index+1]
        right_sorted_aray=Itemcontainer[middle_index+1:rightindex+1]
        k=0;j=0
        for i in range(leftindex,rightindex+1,1):
            print(i,k,j)
            print(left_sorted_aray,right_sorted_aray,Itemcontainer)

            if j>=len(left_sorted_aray) or (k<len(right_sorted_aray) and left_sorted_aray[j]>right_sorted_aray[k]):
                Itemcontainer[i]=right_sorted_aray[k]
                k+=1
            elif k>=len(right_sorted_aray) or (j<len(left_sorted_aray) and  left_sorted_aray[j]<=right_sorted_aray[k]):
                Itemcontainer[i]=left_sorted_aray[j]
                j+=1

if __name__=="__main__":
    sortlist=[23,4,32,545,24,23,1,78,5]
    mergesort(sortlist, 0, 8)
    print(sortlist)
