class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consec = 0
        maxCon = 0
        for num in nums:
            if num == 1:
                consec += 1
                maxCon = max(consec, maxCon)
            else:
                maxCon = max(consec, maxCon)
                consec = 0
            print(maxCon)
        return maxCon