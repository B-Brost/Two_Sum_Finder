class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []

    def bruteForce(self,nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] + nums[i] == target:
                    if i!= j:
                        return (i,j)
                    
    def dictSum(self,nums,target):
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return []
