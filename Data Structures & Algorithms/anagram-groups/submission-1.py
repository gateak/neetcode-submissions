class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_map = {}

        for s in strs:
            word_freq = [0] * 26
            for c in s:
                word_freq[ord(c) - ord("a")] += 1
            key = tuple(word_freq)
            if key not in freq_map:
                freq_map[key] = []
            freq_map[key].append(s)

        return list(freq_map.values())