class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        charFrequencies = {}

        for char in s:
            charFrequencies[char] = charFrequencies.get(char, 0) + 1

        for char in t:
            charFrequencies[char] = charFrequencies.get(char, 0) - 1

        for frequency in charFrequencies.values():
            if frequency != 0:
                return False

        return True