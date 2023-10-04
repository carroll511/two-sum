from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    numbers = {}
    
    for i, num in enumerate(nums):
        find = target - num
        if find in numbers:
            return [numbers[find], i]
        numbers[num] = i

    return []
