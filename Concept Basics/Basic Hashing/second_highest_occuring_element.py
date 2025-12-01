class Solution:
    def secondMostFrequentElement(self, nums):
        dict_ = {}
        res =[]
        for i in nums:
            if i in dict_:
                dict_[i] += 1
            else:
                dict_[i] = 1
        freq_list = sorted(set(dict_.values()))
        if len(freq_list) <2:
            return -1
        second_largest_freq = freq_list[-2]
        res = [k for k,v in dict_.items() if v == second_largest_freq]
        return(min(res))
