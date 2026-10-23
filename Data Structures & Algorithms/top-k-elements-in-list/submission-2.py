class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get frequency of each
        freq_map = {}
        for num in nums:
            if num not in freq_map:
                freq_map[num] = 0
            freq_map[num] += 1

        # bucket them
        buckets = [[] for i in range(len(nums) + 1)]

        for x, y in freq_map.items():
            buckets[y].append(x)

        # traverse backwards
        result = []

        for i in range(len(buckets) - 1, -1, -1):
            for x in buckets[i]:
                if len(result) == k:
                    return result
                result.append(x)
        return result
