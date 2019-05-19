n,m = map(int, raw_input().split())
arr = [map(int, raw_input().split()) for __ in xrange(n)]
brr = [map(int, raw_input().split()) for __ in xrange(n)]
 
for i in xrange(n):
    for j in xrange(m):
        if arr[i][j] > brr[i][j]:
            arr[i][j],brr[i][j] = brr[i][j],arr[i][j]
 
ok = True
def ok(c):
    for i in xrange(n):
        for j in xrange(m):
            if i+1<n and c[i][j] >= c[i+1][j]:
                return False
            if j+1<m and c[i][j] >= c[i][j+1]:
                return False
    return True
 
print "Possible" if ok(arr) and ok(brr) else "Impossible"