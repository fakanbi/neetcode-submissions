class Solution:
    def isPalindrome(self, s: str) -> bool:
        revstring = s[::-1].replace(" ", "").lower()
        revstringAlnum = "".join([char for char in revstring if char.isalnum()])
        print(revstringAlnum)
        string = s.replace(" ", "").lower()
        stringAlnum = "".join([char for char in string if char.isalnum()])
        print(stringAlnum)
        return revstringAlnum == stringAlnum