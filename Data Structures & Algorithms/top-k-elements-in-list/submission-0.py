class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for x in nums:
            if x not in freq_map:
                freq_map[x] = 0
            freq_map[x] += 1

        bucket = [[] for i in range(len(nums) + 1)]

        for x, y in freq_map.items():
            bucket[y].append(x)

        result = []
        for i in range(len(bucket) - 1, -1, -1):
            if not bucket[i]:
                continue
            for x in bucket[i]:
                if len(result) == k:
                    return result
                result.append(x)
        return result
