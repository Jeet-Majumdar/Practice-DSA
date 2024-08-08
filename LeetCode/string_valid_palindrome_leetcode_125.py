"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def check_sc(c):
            asc = c 
            if ((asc >= '0' and asc <= '9') or
                (asc >= 'a' and asc <= 'z') or 
                (asc >= 'A' and asc <= 'Z')):
                return False
            else:
                return True
        r = len(s)-1
        l = 0
        while l < r:
            lstr = s[l]
            rstr = s[r]
            if check_sc(lstr):
                l += 1
                continue
            if check_sc(rstr):
                r -= 1
                continue
            
            if lstr.lower() != rstr.lower():
                return False
            else:
                l += 1
                r -= 1
        return True


"""
## Simple solution

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s1 = ""
        for i in s:
            if i.isalnum():
                s1 += i.lower()
        l = len(s1)
        s2 = ""
        for i in range(1, l+1):
            s2 += s1[l - i].lower()
        
        if s1 == s2:
            return True
        else:
            return False
"""