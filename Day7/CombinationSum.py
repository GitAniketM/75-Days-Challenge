class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def backtrack(candidates, result, diff, path=[], idx=0):
            if diff == 0:
                result.append(path[:])
                return

            for i in range(idx, len(candidates)):
                if candidates[i] > diff:
                    return
                else:
                    diff = diff - candidates[i]
                path.append(candidates[i])
                backtrack(candidates, result, diff, path, i)
                diff += path.pop()

        candidates.sort()
        result = []
        backtrack(candidates, result, target)
        return result