class Solution:
    def isPalindrome(self, s: str) -> bool:
        d = ""
        s = s.lower()
        for char in s:
            if ((char <= 'z' and char >= 'a') or (char <= '9' and char >= '0')):
                d += char

        length = len(d)
        for i in range(length):
            if (d[i] != d[-1-i]):
                return False
        return True