class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in maps:
                return [maps[diff], index]
            maps[num] = index

    