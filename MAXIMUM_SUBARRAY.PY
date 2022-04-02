class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumUpToIdx = 0 
        maxSum = nums[0] 
        for num in nums:
            sumUpToIdx += num
            if sumUpToIdx < num: 
                sumUpToIdx = num
            if maxSum < sumUpToIdx: 
                maxSum = sumUpToIdx
                
        return maxSum
