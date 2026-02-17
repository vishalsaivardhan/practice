# Get min difference solution

def get_min_difference(arr):
    arr.sort()
    min_diff = float('inf')
    for i in range(len(arr) - 1):
        min_diff = min(min_diff, abs(arr[i] - arr[i + 1]))
    return min_diff
