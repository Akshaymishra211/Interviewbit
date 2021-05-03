from bisect import bisect_left
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def binarysearch(self,stack,target):
        l,r=0,len(stack)
        while l<r:
            mid=l+(r-1)//2
            if stack[mid]<target:
                l=mid+1
            else:
                r=mid
        stack.insert(l,target)
        return l
    def smallatright(self,arr):
        res=[0]*len(arr)
        stack=[]
        for i in range(len(arr)-1,-1,-1):
            res[i]=self.binarysearch(stack,arr[i])
        return res
    def solve(self, A, B):
        z=self.smallatright(A)
        cnt=0
        for i in range(len(A)):
            if z[i]>B[A[i]-1]:
                return -1
            else:
                cnt+=z[i]
        return cnt
