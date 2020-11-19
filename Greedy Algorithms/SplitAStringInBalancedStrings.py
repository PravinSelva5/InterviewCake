'''
Balanced strings are those who have equal quantity of 'L' and 'R' characters.
Given a balanced string s split it in the maximum amount of balanced strings.
Return the maximum amount of splitted balanced strings.

---------------------------------------------------------------------------------------------------------------
Runtime: 28 ms, faster than 78.65`%` of Python3 online submissions for Split a String in Balanced Strings.
Memory Usage: 14.1 MB, less than 69.21`%` of Python3 online submissions for Split a String in Balanced Strings.
---------------------------------------------------------------------------------------------------------------
'''
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        max_balanced_string = 0
        counter_R = 0
        counter_L = 0

        # Loop through given array
        
        for letter in s:
            
            if letter == 'R':
                counter_R += 1
            
            if letter == "L":
                counter_L += 1
                
            if (counter_R) == (counter_L):
                max_balanced_string += 1
                counter_R = counter_L = 0
            else:
                continue
        
        return max_balanced_string