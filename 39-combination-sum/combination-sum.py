class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        candidates.sort()
        
        def backtrack(remain: int, combo: list[int], start_index: int):
            if remain == 0:
                results.append(list(combo))
                return
            
            for i in range(start_index, len(candidates)):
                if candidates[i] > remain:
                    break
                
                combo.append(candidates[i])
                backtrack(remain - candidates[i], combo, i)
                combo.pop()
                
        backtrack(target, [], 0)
        return results