# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 23:18:54 2020

@author: Shivam


Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1

"""

def singleNumber(nums):
    v = 0
    for i in nums:
        v = v^i
    return v


ls = [3,4,5,4,5,4,5,4,5]


singleNumber(ls)