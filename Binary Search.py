# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 06:50:34 2023

@author: Bijon
"""

class Solution:
    def searchInSortedList(nums, target)-> int:
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = (lo + hi)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1
    
if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = -1
    result = Solution.searchInSortedList(nums, target)
    print(result)