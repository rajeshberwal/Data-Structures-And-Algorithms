from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    numMap = {}

    for num in nums:
        if num in numMap:
            return True
        numMap[num] = 1
    
    return False