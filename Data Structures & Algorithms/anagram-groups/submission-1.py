class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = {}
        for word in strs:
            if ",".join(sorted(word)) not in my_map:
                my_map[",".join(sorted(word))] = []
            my_map[",".join(sorted(word))].append(word)

        return list(my_map.values())