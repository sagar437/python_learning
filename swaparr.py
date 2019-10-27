def countSwaps(a,n):
    count = 0
    for j in range(n - 1):
        if a[j] < a[j+1]:
#            print(a[j])
            a[j], a[j + 1] = a[j + 1],a[j]
 #           print(a[j])
            count += 1
    print(count)
arr = [1,2,3]
m = 3
countSwaps(arr,m)
