class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        else:
            #t.lower()
            #s.lower()
            list1 = [0 for i in range(26)]
            list2 = [0 for i in range(26)]

            for i in s:
                list1[ord(i)-97]+= 1
            for i in t:
                list2[ord(i)-97]+= 1

            if (list1 != list2):
                return False;
        
        return True