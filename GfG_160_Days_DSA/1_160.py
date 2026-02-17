# Second largest element solution

def second_largest(arr):
    first, second = float('-inf'), float('-inf')
    for number in arr:
        if number > first:
            first, second = number, first
        elif first > number > second:
            second = number
    return second
