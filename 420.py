class Solution:
    def strongPasswordChecker(self, n: str) -> int:

        missing = 3
        missing -= any(a.islower() for a in n)
        missing -= any(a.isupper() for a in n)
        missing -= any(a.isdigit() for a in n)


        repeatedFix = 0
        x = x1 = 0
        i = 2
        while i < len(n):
            if n[i] == n[i-1] == n[i-2]:
                currentLength = 2
                while i < len(n) and n[i - 1] == n[i]:
                    currentLength += 1
                    i += 1
                repeatedFix += currentLength // 3
                x += int(currentLength %3 == 0)
                x1 += int(currentLength %3 == 1)
            else:
                i += 1


        final = max(0, len(n) - 20)
        if len(n) > 20:
            delete = len(n) - 20
            repeatedFix -= min(delete, x)
            delete = max(0, delete - x)
            repeatedFix -= min(delete, x1 * 2) // 2
            delete = max(0, delete - x1 * 2)
            repeatedFix -= delete // 3
        final += max(6 - len(n), missing, repeatedFix)

        return final



passwordCheck = Solution()
print(passwordCheck.strongPasswordChecker('FFFFFFFFFFFFFFF11111111111111111111AAA'))
