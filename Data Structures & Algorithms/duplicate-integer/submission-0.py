class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)):
            if(i == 0):
                tmp = nums[i]
            elif(tmp == nums[i]):
                return True
            else:
                tmp = nums[i]

        return False