class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        numbers = list(set(nums))
        numbers.sort(reverse=True)
        if len(numbers) >= 3:
            return numbers[2]
        else:
            return numbers[0]
