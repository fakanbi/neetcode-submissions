class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
    
        length = len(nums)
        for i in range(len(nums)):
            sumNums = 1
            for j in range(len(nums)):
                if i == j:
                    sumNums = sumNums
                else:
                    sumNums = nums[j] * sumNums
            result.append(sumNums)
        return result