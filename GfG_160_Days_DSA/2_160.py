def pushZerosToEnd(arr):
    c = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[c] = arr[c], arr[i]
            c += 1

if __name__ == "__main__":
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    pushZerosToEnd(arr)
    for num in arr:
        print(num, end=" ")