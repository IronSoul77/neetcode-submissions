class Solution:
    def isPalindrome(self, s: str) -> bool:
        d = ""
        for char in s:
            if ((char <= 'z' and char >= 'a') or (char <= 'Z' and char >= 'A') 
                or (char <= '9' and char >= '0')):
                d += char

        d = d.lower()

        length = len(d)
        for i in range(length):
            if (d[i] != d[-1-i]):
                #print("d[i] =" + d[i] +"d[length-i] =" + d[length - i-1])
                return False
        return True