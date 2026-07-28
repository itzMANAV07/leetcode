class Solution:
    def smallestPalindrome(self, s: str) -> str:
        size=len(s)
        if size%2==0:
            firstHalf=s[:size//2]
            firstHalf= "".join(sorted(firstHalf))
            secondHalf=firstHalf[::-1]
            return firstHalf + secondHalf

        else:
            firstHalf=s[:size//2]
            firstHalf= "".join(sorted(firstHalf))
            secondHalf=firstHalf[::-1]
            midElem=s[size//2]
            return firstHalf + midElem + secondHalf

        