class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        print(frequency)

        sorted_items = sorted(frequency.items(), key=lambda kv: kv[1], reverse=True)
        return [key for key, val in sorted_items[:k]]
        