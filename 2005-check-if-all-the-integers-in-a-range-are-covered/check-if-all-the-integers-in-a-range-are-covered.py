class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        numbers = {}  
        for start, end in ranges:
            i = start
            while i <= end:  
                numbers[i] = True
                i += 1

        i = left
        while i <= right:
            if i not in numbers:
                return False
            i += 1

        return True
