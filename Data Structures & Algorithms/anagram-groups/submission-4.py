class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMaps = {}

        for string in strs:
            hashString = self.hashStr(string)

            if hashString in anagramMaps:
                anagramMaps[hashString].append(string)
            else:
                anagramMaps[hashString] = [string]

        return list(anagramMaps.values())

    def hashStr(self, string: str) -> str:
        key = [0 for _ in range(26)]
        for char in string:
            key[ord(char) - ord('a')] += 1 

        return tuple(key)