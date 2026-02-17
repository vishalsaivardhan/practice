# Max product solution

def max_product(arr):
    max_prod = float('-inf')
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            max_prod = max(max_prod, arr[i] * arr[j])
    return max_prod
