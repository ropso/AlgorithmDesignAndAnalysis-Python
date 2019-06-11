def BinarySearchHelper(item_list,searching_elem,min_index=None,max_index=None):
    if min_index==None and max_index==None:
        min_index=0
        max_index=len(item_list)-1
        return BinarySearch(item_list,searching_elem,min_index,max_index)

def BinarySearch(item_list,searching_elem,min_index,max_index):
    search_index=(min_index+max_index)//2
    if min_index==max_index:
        if searching_elem==item_list[min_index]:
            return min_index
        else:
            return False
    elif item_list[search_index]==searching_elem:
        return search_index
    else:
        if item_list[search_index]>searching_elem:
            return BinarySearch(item_list,searching_elem,min_index,search_index-1)
        elif item_list[search_index]<searching_elem:
            return BinarySearch(item_list,searching_elem,search_index+1,max_index)



if __name__=="__main__":
    test_list=[34,45,56,66,78,81,83,84,90]
    print(BinarySearchHelper(test_list, 93))