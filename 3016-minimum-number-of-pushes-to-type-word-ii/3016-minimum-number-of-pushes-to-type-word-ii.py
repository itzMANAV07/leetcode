class Solution:
    def minimumPushes(self, word: str) -> int:
        frequency = {}
        for ch in word:
            if ch not in frequency:
                frequency[ch] = 1
            else:
                frequency[ch] += 1
        frequency = dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))
        count = 0
        position = 0
        for key in frequency:
            count += frequency[key] * (position // 8 + 1)
            position += 1
        return count