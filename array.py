def reverse_array_in_place(arr):
  n = len(arr)
  for i in range(n // 2):
    arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
arr = [1,2,3,4,5]
reverse_array_in_place(arr)
print(arr)
