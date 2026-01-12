def missingNumber(arr):
        n = len(arr)
        for i in range(n):
            if arr[i] <= 0 or arr[i]> n:
                arr[i] = n+1
        for i in range(n):
            val = abs(arr[i])
            if val <= n:
                arr[val -1] = -abs(arr[val-1])
        for i in range(n):
            if arr[i] > 0:
                return i + 1
        return n + 1
if __name__ == "__main__":
    arr = [2, -3, 4, 1, 1, 7]
    print(missingNumber(arr))