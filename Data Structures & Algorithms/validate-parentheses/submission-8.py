class Solution:
    def isValid(self, s: str) -> bool:
        #if (len(s)%2 != 0):
        #    return False

        #if((s[0] == ']') or (s[0] == '}') or (s[0] == ')')):
        #    return False
        
        stack = []
        myDict = {  '(':')','[':']','{':'}' }

        for paren in s:
            if paren in myDict:
                stack.append(paren)
            else:
                if not stack:
                    return False
                if (myDict[stack[-1]] == paren):
                    stack.pop()
                else:
                    return False
        if stack:
            return False   
             
        return True