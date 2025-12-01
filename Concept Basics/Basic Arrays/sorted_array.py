class Solution:
    def arraySortedOrNot(self, arr, n):
        for i in range(0,n-1):
            for j in range(i+1,n):
                if(arr[i]>arr[j]):
                    return False
        return True
