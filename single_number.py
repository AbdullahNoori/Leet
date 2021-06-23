"""Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space."""


class Solution:
# # #    APPROACH 1: LIST OF OPERATIONS
# singleNumber function takes in arr
# set results to 0
# for loop i in arr
# iterate over all the elements in arr
# print results in numbers are new to array.

    def singleNumber(arr):
        result = 0
        
        for i in arr:
            result ^= i
        return result
            
    arr1 = [4, 3, 3, 4, 1]
    arr2 = [2, 3, 2, 4, 3, 4, 7, 8, 8]


    print(singleNumber(arr1))
    print(singleNumber(arr2))    




    
# APPROACH 2: HASHTABLE
# use hash table to avoid the O(n) time required for searching the elements.
# iterate throug all the elements in nums
# setup key/value pair
# return the element which appeared only once. 

# from collections import defaultdict

# class Solution:
    
#     def singleNumber(self, nums):
#         hash_table = defaultdict(int)
    
   
#         for i in nums:
#             hash_table[i] += 1
            
#         for i in hash_table:
#             if hash_table[i] == 1:
#                 return i
            


#     nums = [4, 3, 3, 4, 1]
#     # nums2 = [2, 3, 2, 4, 3, 4, 7, 8, 8]


#     print(singleNumber(nums))
#     # print(singleNumber(nums2))  