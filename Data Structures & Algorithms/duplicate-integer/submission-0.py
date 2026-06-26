class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        u_nums = set()
        for n in nums:
            if n not in u_nums:
                u_nums.add(n)
            else:
                return True
        return False