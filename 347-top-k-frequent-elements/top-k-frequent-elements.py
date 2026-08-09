class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = {}
        for num in nums:
            groups[num] = groups.get(num, 0) + 1
        
        return sorted(groups, key=groups.get, reverse=True)[:k]