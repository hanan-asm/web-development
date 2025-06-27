class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        num= 1  
        for i in range(len(digits)):
            digits[i] +=num
            if digits[i] < 10:
                num = 0 
                break
            else:
                digits[i] = 0  
        if num == 1:
            digits.append(1)
        return digits[::-1]
