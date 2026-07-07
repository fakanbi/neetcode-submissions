class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # this makes a "list" of all the nums no duplicate
        numSet = set(nums)
        print(numSet)
        longestStreak = 0

        for num in numSet:
            if (num - 1) not in numSet:
                streak = 1
                print("This is the current streak", streak)
                while (num + streak) in numSet:
                    streak += 1
                    print("This is the current streak in the loop", streak)
                longestStreak = max(longestStreak, streak)
        return longestStreak