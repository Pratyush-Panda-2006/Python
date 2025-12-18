arr = [1, 2, 3, 4, 5, 6, 7]
d = 2
n = len(arr)

arr[:d] = reversed(arr[:d])

arr[d:] = reversed(arr[d:])

arr.reverse()
print(arr)