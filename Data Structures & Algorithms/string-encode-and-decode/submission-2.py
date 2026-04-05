class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        strs = []
        pointer = 0
        length = ""
        while pointer < len(s):
            if s[pointer] == "#":
                length = int(length)
                strs.append(s[pointer+1:pointer+1+length])
                pointer = pointer+1+length
                length = ""
            else:
                length += s[pointer]
                pointer += 1

        return strs
