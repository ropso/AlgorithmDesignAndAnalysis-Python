test_case=int(input())
j=0
while j!=test_case:
    j+=1
    input()
    firststring=input()
    secString=input()
    dicfirst=dict()
    dicfirst=dict(zip(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],([0]*26)))
    dicSec=dict(zip(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],([0]*26)))
    for elem in firststring:
        dicfirst[elem]+=1
    for elem in secString:
        dicSec[elem]+=1
    tot_draw=0
    for key,value in dicfirst.items():
        tot_draw+=min(dicSec[key],dicfirst[key])
    print(tot_draw)

