import sys
sys.setrecursionlimit(10**7)
class Solution:
    # @param A : list of integers
    # @return an integer
    def multiply(self,n):
        if n==1:
            return 1
        else:
            return 1+2*self.multiply(n-1)
    def solve(self, A):
        ans=self.multiply(len(A))
        ans=ans%(10**9+7)
        return ans
