class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        
        # we borrow some code from #455:
        players.sort()
        trainers.sort()

        answer = 0
        i = 0
        j = 0
        while i < len(players) and j < len(trainers):
            P = players[i]
            T = trainers[j]
            if P <= T:
                print(f'Player #{i} ({P}) gets trainer #{j} ({T})')
                answer += 1
                i += 1
                j += 1
            else:
                print(f'Nobody wants trainer #{j} ({T})')
                j += 1
        return answer

# NOTE: re-used entire prior version, with variable renames
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 227 ms Beats 5.03%
# NOTE: Memory 33.96 MB Beats 45.90%
