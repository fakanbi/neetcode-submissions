class Solution:

    def encode(self, strs: List[str]) -> str:
        big = ""
        for s in strs:
            big += s + "`"
        if (strs.__len__() == 0):
            return "" 
        return big

    def decode(self, s: str) -> List[str]:
        if (s == ""):
            return []
        strList = []
        curString = ""
        for char in s:
            if char == "`":
                strList.append(curString)
                curString = ""
            else:
                curString += char
        if curString.__len__() != 0:
            strList.append(curString)
        return strList



