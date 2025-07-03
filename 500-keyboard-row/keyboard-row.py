class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        output = []
        for word in words:
            letter = set(word.lower())
            if letter.issubset(row1) or letter.issubset(row2) or letter.issubset(row3):
                output.append(word)
        return output




        