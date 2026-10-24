class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #strsnew = strs.copy()
        #groups = {}

        #for i in range(len(strsnew)):
        #    strsnew[i] = "".join(sorted(strs[i]))

        #for i in range(len(strsnew)):
        #    key = strsnew[i]

        #    if key not in groups:
        #        groups[key] = []
        #    groups[key].append(i)

        #result = []
        
        #for indices in groups.values():
        #    temp = []
        #    for i in indices:
        #        temp.append(strs[i])
        #    result.append(temp)

        #return result

        groups={}

        for word in strs:
            key = "".join(sorted(word))

            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        
        return list(groups.values())

