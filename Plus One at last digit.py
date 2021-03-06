
"""
66. Plus One
Easy

1895

2736

Add to List

Share
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Example 3:

Input: digits = [0]
Output: [1]
 

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
Accepted
725,766
Submissions
1,695,401

"""


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        if digits[0] == 9 and len(digits) == 1:
            return [1,0]
        
        x = digits.pop() + 1
        if x == 10:
            new_d = self.plusOne(digits)
            new_d.append(0)
            return new_d
        else:
            digits.append(x)
        return digits