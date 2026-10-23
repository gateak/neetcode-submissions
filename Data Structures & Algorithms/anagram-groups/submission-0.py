class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_map = {}

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1

            key = tuple(count)
            if key not in freq_map:
                freq_map[key] = []
            freq_map[key].append(s)

        return list(freq_map.values())