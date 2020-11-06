class Solution:
    def twoSum(self, nums, target):
        """
        The function inputs are list of integers and an target integer
        Function then scan an array for numbers wich will add up to make a target integer
        Output is a list of indices of those numbers in a list
        """
        numbers = {}
        for i, num in enumerate(nums):
            if target - num in numbers:
                return [numbers[target-num], i]
            numbers[num] = i
        return []