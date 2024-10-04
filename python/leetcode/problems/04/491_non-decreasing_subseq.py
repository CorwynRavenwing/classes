class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        possibles = set()
        for N in nums:
            N_tuple = (N,)
            new_possibles = {
                P + N_tuple
                for P in possibles
                if P[-1] <= N
            }
            new_possibles.add(N_tuple)  # this number in a tuple by itself
            print(f'{new_possibles=}')
            possibles |= new_possibles
        answers = {
            P
            for P in possibles
            if len(P) > 1
        }
        return sorted(answers)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 165 ms Beats 20.83%
# NOTE: Memory 23.88 MB Beats 95.38%
