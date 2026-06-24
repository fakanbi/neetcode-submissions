class Solution:
    def isPalindrome(self, s: str) -> bool:
        revstring = s[::-1].replace(" ", "").lower()
        revstringAlnum = "".join([char for char in revstring if char.isalnum()])
        string = s.replace(" ", "").lower()
        stringAlnum = "".join([char for char in string if char.isalnum()])
        return revstringAlnum == stringAlnum