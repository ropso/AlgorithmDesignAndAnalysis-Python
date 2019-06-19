def countinversion(item_container,lower_index,upper_index):
    if lower_index==upper_index:
        return 0
    middle_index=(lower_index+upper_index)//2
    left_inverion=countinversion(item_container,lower_index,middle_index)
    right_inversion=countinversion(item_container,middle_index+1,upper_index)
    split_inversion=0
    leftindex=0;rightindex=0
    left_sorted_aray=item_container[lower_index:middle_index+1]
    right_sorted_aray=item_container[middle_index+1:upper_index+1]
    for i in range(lower_index,upper_index+1):
        if rightindex>=len(right_sorted_aray) or (leftindex<len(left_sorted_aray)  and left_sorted_aray[leftindex]<right_sorted_aray[rightindex]):
            item_container[i]=left_sorted_aray[leftindex]
            leftindex+=1
        elif leftindex>=len(left_sorted_aray) or (rightindex<len(right_sorted_aray) and right_sorted_aray[rightindex]< left_sorted_aray[leftindex]):
            item_container[i]=right_sorted_aray[rightindex]
            rightindex+=1
            split_inversion+=len(left_sorted_aray)-leftindex
    return left_inverion+right_inversion+split_inversion

if __name__=="__main__":
    item=[]
    for i in range(1,100001):
        item.append(int(input()))
    print(item)
    items=[1,4,2,5,7,6,10,8]

    print(len(item))
    print(countinversion(item,0,len(item)-1))



