"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'

"""


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1 or len(s) > 10**4:
            return False
        if s is None:
            return False
        else:
            stack = []
            
            mapping = {")":"(",
                      "}":"{",
                      "]":"["}
            
            for char in s:

            # If the character is an closing bracket
                if char in mapping:

                    # Pop the topmost element from the stack, if it is non empty
                    # Otherwise assign a dummy value of '#' to the top_element variable
                    top_element = stack.pop() if stack else '#'

                    # The mapping for the opening bracket in our hash and the top
                    # element of the stack don't match, return False
                    if mapping[char] != top_element:
                        return False
                else:
                    # We have an opening bracket, simply push it onto the stack.
                    stack.append(char)

            # In the end, if the stack is empty, then we have a valid expression.
            # The stack won't be empty for cases like ((()
            return not stack