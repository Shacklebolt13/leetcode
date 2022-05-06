class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = [x.lower() for x in s if x.isalnum()]
        print(s)
        print(s[::-1])
        return s == s[::-1]