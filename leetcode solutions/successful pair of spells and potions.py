# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/
from typing import List
import bisect

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        result = []
        
        for spell in spells:
            min_potion_required = success / spell
            index = bisect.bisect_left(potions, min_potion_required)
            result.append(len(potions) - index)
        
        return result

spells = list(map(int, input().split()))  
potions = list(map(int, input().split()))  
success = int(input())  
solution = Solution()
print(solution.successfulPairs(spells, potions, success))
