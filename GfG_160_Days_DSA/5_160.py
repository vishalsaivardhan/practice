class Solution:
    def nextPermutation(self, arr):
        n = len(arr)
        p = -1
        for i in range(n - 2,-1,-1):
            if arr[i] < arr[i + 1]:
                p = i
                break
        if p == -1:
            arr.reverse();
            return
        for i in range(n -1,p,-1):
            if arr[i]> arr[p]:
                arr[i],arr[p] = arr[p],arr[i]
                break
        left,right = p+1,n-1
        while left < right:
            arr[left],arr[right]=arr[right],arr[left]
            left +=1
            right -=1
        return arr
s=Solution()
a =[2,4,5,0,1,7]
print(s.nextPermutation(a))