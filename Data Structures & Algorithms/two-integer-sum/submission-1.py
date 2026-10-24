class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        ans = [0,0]
        for i in range(size):
            for j in range(i+1, size):
                if (target == nums [i] + nums[j]):
                    ans[0] = i
                    ans[1] = j
                    return ans


        