class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.data = []
        votes = Counter()
        current_winner_id = None
        current_winner_votes = 0
        for (person, time) in zip(persons, times):
            votes[person] += 1
            if current_winner_votes <= votes[person]:
                current_winner_votes = votes[person]
                if current_winner_id != person:
                    current_winner_id = person
                    print(f'{time=}, winner now #{person} with {current_winner_votes} v')
            self.data.append(
                (time, current_winner_id, current_winner_votes)
            )
        print(f'{self.data=}')
        return
    
    def q(self, t: int) -> int:
        index = bisect_left(self.data, (t, 0, 0))
        print(f'q({t}): {index=}')
        if index >= len(self.data):
            index -= 1
            print(f'  MAX:{index=}')
        Q = self.data[index]
        print(f'  {Q=}')
        (time, winnerID, winnerCount) = Q
        if time > t:
            index -= 1
            print(f'  DOWN:{index=}')
            assert index >= 0
            Q = self.data[index]
            print(f'  -> {Q=}')
            (time, winnerID, winnerCount) = Q
        print(f'at {time=} <= {t}, winner was {winnerID} with {winnerCount} votes')
        return winnerID

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
