import math
def nearestPair(px,py):
    '''recursive algorithm to find the nearest poair of points in a plane complexity=nlg(n)
    base case when there are 4 points use linear search and return min pair distance'''
    if len(px)<=4:
        min_distance=[-1,[0,0]]
        for i in range(0,len(px)):
            for j in range(i+1,len(px)):
                delta=math.sqrt(((px[i][1][0]-px[j][1][0])**2)+((px[i][1][1]-px[j][1][1])**2))
                if delta<min_distance[0]:
                    min_distance=[delta,[px[i],px[j]]]
        return min_distance

    else:
        print(px)
        print(py)
        middle_index=len(px)//2
        #there are 2 cases 
        nearest_pair_in_left=nearestPair(px[:middle_index+1],py[:middle_index+1])
        nearest_pair_in_right=nearestPair(px[middle_index+1:],py[middle_index+1:])
        delta=min(nearest_pair_in_left[0],nearest_pair_in_right[0])
        closetSplitPair(px,py,delta)

def closetSplitPair(px,py,delta):
    '''1 want o(n) time 2. dont need to always copete in the distance where dictance less then delta
    step1> pruning a.take the middle x coordinate 
    remove all elemnts in range of delta and make a set s_y conatininall elemnet satisying above conditions
    and sorted in order of y 
    3 now iterate over s_y and look over the index upto next till y > delta 
    at the same time find the delta '''
    avg_x=(px[-1][0]+px[0][0])/2
    best=delta 
    pair=0
    element_subset=[i for i in py if abs(avg_x-py[1][0])<=delta]
    for i in range(0,len(element_subset)):
        for j in range(1,min(7,(len(element_subset)-i))):
            pair_delta=math.sqrt(((element_subset[i][1][0]-element_subset[j][1][0])**2)+((element_subset[i][1][1]-element_subset[j][1][1])**2))
            if pair_delta<delta:
                best=pair_delta
                pair=[best,[element_subset[i],element_subset[j]]]
    return pair


def nearest_pair_naive(arr,right_index,left_index):
    '''o(n^2)'''
    for i in range(0,right_index):
        for j in range():
            pass


if __name__=="__main__":
    test_item_container=[[2,3],[1,2],[4,5],[6,2],[8,10],[57,89],[66,90],[99,12],[12,12],[13,17]]
    sorted_list_on_x=[]
    sorted_list_on_y=[]
    for elem in test_item_container:
        sorted_list_on_x.append([elem[0],elem]),sorted_list_on_y.append([elem[1],elem])
    sorted_list_on_x=sorted(sorted_list_on_x,key=lambda x: x[0])
    sorted_list_on_y=sorted(sorted_list_on_y,key=lambda x: x[0])
    nearestPair(sorted_list_on_x,sorted_list_on_y)
