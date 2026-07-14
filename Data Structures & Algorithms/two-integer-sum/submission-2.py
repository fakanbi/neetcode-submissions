class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # store in a dictionary with index and num
        seen = {}

        for i, num in enumerate(nums):
            seen[num] = i
        for i, num in enumerate(nums):
            difference = target - num
            if difference in seen and seen[difference] != i:
                return [i, seen[difference]]
        return []