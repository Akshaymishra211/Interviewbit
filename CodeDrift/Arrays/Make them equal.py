class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        l=[]
        index,cnt,m=0,0,len(A)
        for i in range(m):
            temp=bin(A[i])[2:]
            l.append(temp)
        for i in range(32):
            if i>len(l[0])-1:
                index=i
                break
            else:
                x=l[0][i]
            for j in range(m):
                if i>len(l[j])-1 or l[j][i]!=x:
                    index=i
                    break
            else:
                continue
            break
        for i in range(m):
            cnt+=(len(l[i])-index)
        return cnt
