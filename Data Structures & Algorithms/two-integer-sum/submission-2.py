class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rns = {}
        for i, num in enumerate(nums):
            if num in rns:
                return [rns[num], i]
            else:
                rn = target - num
                rns[rn] = i
        return [0, 0]