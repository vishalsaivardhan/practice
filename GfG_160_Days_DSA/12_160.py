# Max circular sum solution

def max_circular_sum(arr):
    max_straight_sum = max_subarray_sum(arr)
    total_sum = sum(arr)
    inverted_array = [-x for x in arr]
    max_inverted_sum = max_subarray_sum(inverted_array)
    max_circular_sum = total_sum + max_inverted_sum
    return max(max_straight_sum, max_circular_sum)
