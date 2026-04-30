from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=defaultdict(list)
        for i in strs:
            key="".join(sorted(i))
            ans[key].append(i)
        return list(ans.values()) 

OUTPUT:
Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

ANOTHER METHOD:
a=["eat","tea","tan","ate","nat","bat"]
ans={}
for i in a:
    key="".join(sorted(i))
    if key not in ans:
        ans[key]=[]
    ans[key].append(i)
print(list(ans.values()))  
