class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        
        if len(votes) == 1:
            # shortcut for only-one-voter situation
            return votes[0]
        
        teams = list(votes[0])
        teams.sort()    # not really necessary
        print(f'{teams=}')
        
        vote_counts_by_rank = [
            Counter(rank_N)
            for rank_N in zip(*votes)
        ]
        print(f'{vote_counts_by_rank=}')

        vote_counts_by_team = {
            team: tuple([
                vote_counts[team]
                for vote_counts in vote_counts_by_rank
            ])
            for team in teams
        }
        print(f'{vote_counts_by_team=}')

        BY_VOTE_COUNTS_ASC_THEN_TEAM_NAME_DESC = lambda T: (vote_counts_by_team[T], -ord(T))
        teams.sort(
            key=BY_VOTE_COUNTS_ASC_THEN_TEAM_NAME_DESC,
            reverse=True
        )

        return ''.join(teams)

# NOTE: Accepted on first Submit
# NOTE: Runtime 10 ms Beats 96.67%
# NOTE: Memory 17.08 MB Beats 22.72%
