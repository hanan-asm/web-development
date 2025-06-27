class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        arr = [list(row) for row in strs]
        numrow = len(arr)
        numcol = len(arr[0])
        delete = 0
        for col in range(numcol):
            for row in range(1, numrow):
                if arr[row][col] < arr[row - 1][col]:
                    delete += 1
                    break  
        return delete

        