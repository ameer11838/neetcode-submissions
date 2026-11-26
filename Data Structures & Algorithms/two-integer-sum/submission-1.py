class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       maped = {}
       for i, n in enumerate(nums):
        diff = target - n
        if diff in maped:
            return [maped[diff], i]
        maped[n] = i



    