class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #for i in range(len(nums)):
        #    for j in range(i+1, len(nums)):
        #        if (target == nums [i] + nums[j]):
        #            return [i,j]

        seen = {} # a dictionary
        for i, num in enumerate(nums): #enumerate means gives boht index (i) nd value (num)
            complement = target - num #we're looking for complement in dictionary

            if complement in seen: #checks if the needed value (complement) is a key in the dict
                return [seen[complement], i] 
                #returns the value stored at the matched key and the index of current num
                #return as (i,j)
            
            seen[num] = i 
            #else store a new key value pair, num (key)(complement) : i (value)(index)

