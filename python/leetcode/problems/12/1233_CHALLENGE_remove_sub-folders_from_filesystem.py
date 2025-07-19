class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        folder.sort()

        answer = []
        
        while folder:
            F = folder.pop(0)
            answer.append(F)
            folder = [
                SF
                for SF in folder
                if not SF.startswith(F + '/')
            ]
        
        return answer

# NOTE: Accepted on second Run (first was set.add/list.append mixup)
# NOTE: Accepted on first Submit
# NOTE: Runtime 2209 ms Beats 5.00%
# NOTE: Memory 29.69 MB Beats 39.14%

# NOTE: re-ran for challenge:
# NOTE: Runtime 2390 ms Beats 5.08%
# NOTE: Memory 30.54 MB Beats 77.01%
