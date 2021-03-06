from typing import List


# Description: Given an array of integers, return indices of the two numbers
def twoSum(nums: List[int], target: int) -> List[int]:
    numMap = {}

    for i, num in enumerate(nums):
        diff = target - num

        if diff in numMap:
            return [numMap[diff], i]
        else:
            numMap[num] = i
    return None
