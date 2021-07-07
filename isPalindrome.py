''' Write a Python Program to check whether a string is a Palindrom or not. 
    (Hint: A paindrome ais a word, phrase, number or sequence of 
    words that reads the same backward as forward...e.d: Madam '''




def isPalindrome(s):
    
    # Use predefined function to 
    # reverse to string print(s)
    rev = ''.join(reversed(s))

    # Checking if both string are equal or not
    if (s == rev):
        return True
    return False

isPalindrome("madam")