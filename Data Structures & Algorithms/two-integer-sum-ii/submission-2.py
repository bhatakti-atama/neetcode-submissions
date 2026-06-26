class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        curr_sum = numbers[l] + numbers[r]
        while  curr_sum != target:
            if curr_sum > target:
                r -= 1
            if curr_sum < target:
                l += 1
            curr_sum = numbers[l] + numbers[r]
        return [l + 1, r + 1]