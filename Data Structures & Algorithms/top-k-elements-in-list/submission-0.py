class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        u_nums = {}
        for num in nums:
            if num in u_nums:
                u_nums[num] += 1
            else:
                u_nums[num] = 1
        k_elements = sorted(u_nums, key = u_nums.get, reverse = True)[:k]
        return k_elements