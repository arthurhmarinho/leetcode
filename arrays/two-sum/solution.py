"""
two-sum
https://leetcode.com/problems/two-sum/
"""
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Retorna os índices de dois números em nums que somam target.
    Tempo: O(n) | Espaço: O(n)
    """
    seen = {}

    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i

    return []


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
    print(two_sum([3, 2, 4], 6))       # [1, 2]
    print(two_sum([3, 3], 6))          # [0, 1]
