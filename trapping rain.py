class Solution:
    def trap(self, height: List[int]) -> int:
        n=[]
        maxi=height[0]
        for i in height:
            maxi=max(maxi,i)
            n.append(maxi)
        a=[]
        maxa=height[-1]
        for j in height[::-1]:
            maxa=max(maxa,j) 
            a.append(maxa)
        b=a[::-1]
        s=[]
        for i in range(0,len(n)):
            mini=min(n[i],b[i])
            s.append(mini)
        m=[] 
        for j in range(0,len(height)):
            d=s[j]-height[j]
            m.append(d)
        return sum(m)    

OUTPUT:
Example 1:



Input: height = [0,2,0,3,1,0,1,3,2,1]

Output: 9

        
