class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nMap = {}
        for n in range(len(nums)):
            guh = target-nums[n]
            if guh in nMap:
                return [nMap[guh], n]
            nMap[nums[n]] = n