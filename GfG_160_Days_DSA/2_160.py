# Push zeros to end solution

def push_zeros_to_end(arr):
    count = 0  # Count of non-zero elements
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
    while count < len(arr):
        arr[count] = 0
        count += 1
