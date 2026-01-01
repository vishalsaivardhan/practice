# Day 1 of 160
#second largest element of an array
class Solution:
    def getSecondLargest(self,arr):
        n = len(arr)
        if n < 2:
            return -1
        f = s = float('-inf')
        for num in arr:
            if num > f:
                s = f
                f = num
            elif num > s and num < f:
                s = num
        if s == float('-inf'):
            return -1
        else:
            return s
a = [12, 34, 10, 35, 35]
sol = Solution()
print(sol.getSecondLargest(a))