class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consec = 0
        maxCon = 0
        for num in nums:
            if num == 1:
                consec += 1
                if consec > maxCon:
                    maxCon = consec
            else:
                if consec > maxCon:
                    maxCon = consec
                consec = 0
            print(maxCon)
        return maxCon