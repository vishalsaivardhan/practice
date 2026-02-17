# Find majority elements solution

def find_majority_element(arr):
    count = 0
    candidate = None
    for element in arr:
        if count == 0:
            candidate = element
        count += (1 if element == candidate else -1)
    return candidate if arr.count(candidate) > len(arr) // 2 else None
