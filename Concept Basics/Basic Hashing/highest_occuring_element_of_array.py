class Solution:
    def mostFrequentElement(self, nums):
        _dict = {}
        for i in nums:
            if i in _dict:
                _dict[i] += 1
            else:
                _dict[i] = 1
        max_freq = max(_dict.values())
        res = [k for k,v in _dict.items() if v == max_freq]
        return min(res)