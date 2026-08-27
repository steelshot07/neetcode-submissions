class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        las = []
        i=0
        while i<len(nums):
            if nums[i] in las:
                return nums[i]
            else:
                las.append(nums[i])
            i+=1