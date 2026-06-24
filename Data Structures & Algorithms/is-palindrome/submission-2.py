class Solution:
    def isPalindrome(self, s: str) -> bool:
        revstring = s[::-1].replace(" ", "").lower()
        revstringAlnum = "".join([char for char in revstring if char.isalnum()])
        return revstringAlnum == revstringAlnum[::-1]