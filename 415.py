class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        number1 = 0
        number2 = 0
        for digit in num1:
            number1 *= 10
            for d in '0123456789':
                number1 += digit > d

        for digit in num2:
            number2 *= 10
            for d in '0123456789':
                number2 += digit > d

        return str(number1 + number2)
