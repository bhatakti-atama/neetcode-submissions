class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while numbers[l] + numbers[r] != target:
            curr_sum = numbers[l] + numbers[r]
            diff = target - curr_sum
            if diff < 0:
                r -= 1
            if diff > 0:
                l += 1
        return [l + 1, r + 1]