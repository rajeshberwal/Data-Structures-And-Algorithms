from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    n = len(nums)
    return sum(nums) == (n * (n + 1)//2)