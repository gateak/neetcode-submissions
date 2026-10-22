class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nmap = {num: index for index, num in enumerate(nums)}
        
        for index, num in enumerate(nums):
            complement = target - num
            if complement in nmap and nmap[complement] != index:
                return [index, nmap[complement]]
        return []