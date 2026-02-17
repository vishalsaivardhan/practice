# Rotate array solution

def rotate_array(arr, d):
    n = len(arr)
    d = d % n  # In case the rotating factor is greater than n
    return arr[d:] + arr[:d]
