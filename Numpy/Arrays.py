import numpy

def arrays(arr):
    a = numpy.array(arr,float)
    b = numpy.array(arr,float)
    n = a.size
    for i in range(n):
        b[n-i-1] = arr[i]
    return b

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
