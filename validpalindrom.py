class Solution:
    def isPalindrome(self, s: str) -> bool:
        b=s.lower()
        a=""
        for i in b:
            if(i.isalpha() or i.isdigit()):
                a+=i
        if(a[::-1]==a):
            return True
        else:
            return False         

OUTPUT:
Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false
Explanation: "tabacat" is not a palindrome.
