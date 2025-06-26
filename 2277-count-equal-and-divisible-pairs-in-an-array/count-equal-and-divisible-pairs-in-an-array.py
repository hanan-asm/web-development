class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        index = {}
        count = 0
        for idx, val in enumerate(nums):
            if val not in index:
                index[val] = []
            index[val].append(idx)
        for indices in index.values():
            size = len(indices)
            for i in range(size):
                for j in range(i + 1, size):
                    if (indices[i] * indices[j]) % k == 0:
                        count += 1
        return count

        