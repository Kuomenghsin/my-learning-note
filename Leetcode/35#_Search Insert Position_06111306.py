class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        now = 0
        if len(nums)-1 != 0:
            for i in range(len(nums)-1):
                if target not in nums:
                    if i == 0 and target < nums[i]:
                        return now
                    if target > nums[i] and target < nums[i+1]:
                        now+=1
                        return now
                    if target > nums[i] and target > nums[i+1] and i+1 != len(nums)-1:
                        now+=1
                    if target > nums[i+1] and i+1 == len(nums)-1:
                        now+=2
                        return now
                else:
                    for i in range(len(nums)):
                        if target == nums[i]:
                            return i
        else:
            if target > nums[0]:
                return 1
            if target < nums[0]:
                return 0
            if target == nums[0]:
                return 0
