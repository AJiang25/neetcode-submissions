class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
 
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        # i = where the next encoded word begins.
        # j = where the next # is located.
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) 
            i = j + 1 # move i to the beginning of the word
            j = i + length # move j to the end of the word (aka word + 1)
            res.append(s[i:j]) # append the word
            i = j # reset i and j 
        return res
