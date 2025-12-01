""" 
Problem => Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "". 

Examples:
Input : str = ["flowers" , "flow" , "fly", "flight" ]
Output : "fl"

Explanation :
All strings given in array contains common prefix "fl".

Input : str = ["dog" , "cat" , "animal", "monkey" ]
Output : ""

Explanation :
There is no common prefix among the given strings in array.

Input : str = ["lady" , "lazy"]
Output:"la"

"""

# code

class Solution:  
    def longestCommonPrefix(self, st):
        res = ""
        sorted_arr = sorted(st)
        fw = sorted_arr[0]
        lw = sorted_arr[-1]
        for ch in range (min(len(fw),len(lw))):
            if(fw[ch] != lw[ch]):
                break 
            res += fw[ch]
        return res

