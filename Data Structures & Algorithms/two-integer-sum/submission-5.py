class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for x,y in enumerate(nums):
            complement = target - y
            if complement in seen and x != seen[complement]:
                return [seen[complement], x]
            seen[y] = x
        return []