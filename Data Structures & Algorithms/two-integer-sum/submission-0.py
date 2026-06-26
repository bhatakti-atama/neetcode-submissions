class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rns = {}
        for i in range(len(nums)):
            if nums[i] in rns.keys():
                return [rns[nums[i]], i]
            else:
                rn = target - nums[i]
                rns[rn] = i
        return [0,0]