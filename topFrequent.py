from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=Counter(nums)
        a=[]
        for i in n.most_common(k):
            a.append(i[0])
        return a 

OUTPUT:
Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7]
