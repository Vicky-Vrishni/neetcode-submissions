class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1

        found = False
        for i in dict.values():
            if i>1:
                found = True

        return found