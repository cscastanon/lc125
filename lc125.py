#Leetcode # 125 | Valid Palindrome
#My solution: 4/10/2023
#Problem Difficulty Level: Easy
#Solution 1

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        fixedStr = ""
        for c in s:
            fixedStr += c.lower()
        print(fixedStr)
        fx2 = re.sub(r'[^a-zA-Z0-9]', '', fixedStr)
        print("fixed=",fx2)

        l = 0
        for r in range(len(fx2)-1, -1, -1):
            if fx2[l] == fx2[r]:
                print(fx2[l], " == ", fx2[r])
                l += 1
            else:
                return False
        return True
