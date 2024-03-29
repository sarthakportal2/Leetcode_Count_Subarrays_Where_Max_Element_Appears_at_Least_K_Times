from bisect import bisect_left#importing bisect_left liberary 
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        #T(C(N)==O(N)) and S(C(N)=O(N) as it requires non contigours memory alloc iteratively
        pre=[0]#pre array list declare
        mi=max(nums)#maximizing the nums list 
        out=0#output initialize
        for i in range(len(nums)):#nums length iteration
            pre.append(pre[-1]+int(nums[i]==mi))#appending pre list with maximum sub array elements
            j=bisect_left(pre,pre[-1]-k+1)#bisecting array list's sorting  
            j-=1#decremtning bisected array's element
            if j>=0:out+=j+1#incrementing output  list
            
        return out#printing output subarray
