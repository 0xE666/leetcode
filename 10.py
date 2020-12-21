import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        match = re.findall(p, s)
        if match:
            if match[0] == s:
                return True
            else:
                return False
        else:
            return False
