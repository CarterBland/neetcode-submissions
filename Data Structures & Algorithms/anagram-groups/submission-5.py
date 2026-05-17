class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for string in strs:
            key = self.anagramKey(string)
            if key in anagrams:
                anagrams[key].append(string)
            else:
                anagrams[key] = [string]

        return list(anagrams.values())

    def anagramKey(self, toKey: str) -> str:
        arr = [0] * 26

        for char in toKey:
            arr[ord(char) - ord('a')] += 1

        return str(arr)