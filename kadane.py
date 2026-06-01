def kadane(arr):
    max_ending = arr[0]#-2
    max_so_far = arr[0]#-2

    for x in arr[1:]:
        max_ending = max(x,max_ending + x)
        max_so_far = max(max_so_far, max_ending)

    return max_so_far

arr=[2, 3, -8, 7, -1, 2, 3]
print("Max Subarray Sum =", kadane(arr))
