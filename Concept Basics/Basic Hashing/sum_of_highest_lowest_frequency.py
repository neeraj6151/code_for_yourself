class Solution:
    def sumHighestAndLowestFrequency(self, nums):
        dict_ = {}
        for i in nums:
            if i in dict_:
                dict_[i] += 1
            else:
                dict_[i] = 1
        res = sorted(list(dict_.values()))
        return res[0] + res [-1]
       