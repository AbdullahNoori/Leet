''''Given an array of integers nums which is sorted in ascending order, 
    and an integer target, write a function to search target in nums. 
    If target exists, then return its index. Otherwise, return -1.'''
    
'''You must write an algorithm with O(log n) runtime complexity.'''

class Solution(object):
      
# What data structure will you use to store a modifiable collection?
# store data collection, access it, insert it, modify data collection

# ARRAY -
# Time complexity: 
# search(n) = O(n)
# insert(n) = 0(1)
# remove(n) = O(n)

# lINKEDLIST -
# Time complexity:
# # search(n) = O(n)
# insert(n) = 0(1)
# remove(n) = O(n)

# ARRAY SORTED -
# Time complexity:
# # search(n) = O(logn)
# insert(n) = 0(n)
# remove(n) = O(n)


# BINARY SEARCH - (much faster for larger data collection searchs ex: 100M)
# Time complexity:
# # search(n) = O(logn)
# insert(n) = 0(1ogn)
# remove(n) = O(logn)

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1
    
target = 10
    
nums = [-2, 0, 1, 5, 4, 8, 10, 15, 18]

