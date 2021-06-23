#!/usr/bin/env python3

"""Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not."""



# class Solution:


#     def isHappy(self, n: int) -> bool:
#         if (n == 1):
#             return true:
    
#         elif (n == 4):
#                 return false;
            
#         else:
#             return isHappy(toSumOfSquares(n));



class Solution:
    
    # def isHappy(self, n: 19):
        
    #     def get_next(number):
    #         total_sum = 0
    #         while number > 0:
    #             number, digit = divmod(number, 10)
    #             total_sum += digit ** 2
    #         return total_sum
        
    #     while n != 1 and n != 4:
    #         n = get_next(n)
            
    #     return n == 1
    
    def isHappy(self, n):
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.toSumOfSquares(n)

            if n ==1:
                return True
            
        return False 
        