class Solution:
    def setBuilder(self, ptr :int, nums: List[int], curr_set: List[List], curr_sub_set: List):
        if ptr < len(nums):
            p0 = curr_sub_set.copy()
            p0.append(nums[ptr])
            p1 = curr_sub_set.copy()
            ptr += 1
            self.setBuilder(ptr, nums, curr_set, p0)
            self.setBuilder(ptr, nums, curr_set, p1)
        else:
            return curr_set.append(curr_sub_set)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.setBuilder(0, nums, res, [])
        return res