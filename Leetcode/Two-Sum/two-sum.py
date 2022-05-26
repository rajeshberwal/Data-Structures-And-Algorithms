from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    numMap = {}

    for i, num in enumerate(nums):
        diff = target - num

        if diff in numMap:
            return [numMap[diff], i]
        else:
            numMap[num] = i
    return None
