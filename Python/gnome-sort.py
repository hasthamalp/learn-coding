def gSort( arr, a):
    i = 0
    while i < a:
        if i == 0:
            i= i+ 1
        if arr[i] >= arr[i- 1]:
            i= i+ 1
        else:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i= i- 1

    return arr

arr = [9, 34, 1, -3]
a = len(arr)

arr = gSort(arr, a)
print "Elements in Gnome Sort :",
for i in arr:
    print i,
