class Solution:
    def romanToInt(self, s: str) -> int:
        s = s[::-1]

        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0
        prev = 0

        for ch in s:
            curr = values[ch]

            if curr < prev:
                total -= curr
            else:
                total += curr

            prev = curr

        return total