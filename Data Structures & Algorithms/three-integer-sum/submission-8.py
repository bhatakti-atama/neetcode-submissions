class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for p in range(len(nums) - 2):
            # Early exit: if the current number is > 0, sum cannot be zero
            if nums[p] > 0:
                break
            
            # Skip duplicates for the anchor element
            if p > 0 and nums[p] == nums[p - 1]:
                continue
                
            l = p + 1
            r = len(nums) - 1
            
            while l < r:
                currSum = nums[p] + nums[l] + nums[r]
                
                if currSum > 0:
                    r -= 1
                elif currSum < 0:
                    l += 1
                else:
                    # Found a triplet, append directly to list
                    res.append([nums[p], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    
                    # Skip duplicates for the left and right pointers
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                        
        return res