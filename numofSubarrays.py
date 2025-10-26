class Solution(object):
    def numOfSubarrays(self, arr, k, t):
        n=len(arr)
        if n<k:
            return 0
        c=0
        s=sum(arr[0:k])
        if s>=t*k:
            c=c+1
        for i in range(k,n):
            s=s+arr[i]
            s=s-arr[i-k]
            if s>=t*k:
                c=c+1
        return c
