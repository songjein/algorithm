class Solution:
    def checkSubarraySum(self, nums, k):

        for start in range(len(nums)):
            total = 0
            for end in range(start, len(nums)):
                total += nums[end]
                if end - start + 1 < 2:
                    continue
                    
                if k == 0:
                    if (total == k):
                        return True
                else:
                    if (total % k == 0):
                        return True
                
        return False
