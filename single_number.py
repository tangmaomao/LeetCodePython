# 1. Sort the array
# 2. The special number can only locate on even location
#    like 0, 2, 4, 6 ...
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
    	A.sort()
    	if len(A) == 1:
    	    return A[0]
    	for i in range(0,len(A)-1,2):
    		
    			if A[i] != A[i+1]:
    				return A[i]
    		
    	if A[len(A)-1] != A[len(A)-2]:
    		return A[len(A)-1]