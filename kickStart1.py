test_case=int(input())
j=0
while j!=test_case:
    j+=1
    tot_stu,tot_selection=[int(i) for i in input().split(" ")]
    stu_pow_list=[int(i) for i in input().split(" ")]
    stu_pow_list.sort(reverse=True)
    
    i=0
    prior_train_time=0
    for i in range(0,tot_selection):
        prior_train_time+=stu_pow_list[0]-stu_pow_list[i]
    least_train_time=prior_train_time
    i=1
    while(i<(tot_stu-tot_selection+1)):
        tmp=(prior_train_time-((stu_pow_list[i-1]-stu_pow_list[i])*(tot_selection-1)))+(stu_pow_list[i]-stu_pow_list[i+tot_selection-1])
        if tmp<least_train_time:
            least_train_time=tmp
        prior_train_time= tmp
        i+=1
    print("Case #{}: {}".format(j,least_train_time))
# 4 3
# 3 1 9 100
# 6 2
# 5 5 1 2 3 4
# 5 5
# 7 7 1 7 7