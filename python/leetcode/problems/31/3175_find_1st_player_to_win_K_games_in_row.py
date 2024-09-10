class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:

        # SHORTCUT:
        # Say players A and B are first and second in the queue.
        # Say player B wins, and player A is sent to the back.
        # I'm pretty sure we never see player A again; if we do,
        # the person he will face is either player B (who beat him),
        # or another player who *beat* player B later, or someone
        # who beat *that* person, and so forth: therefore A will
        # definitely always lose all future games.
        #   Therefore, we can actually *delete* player A, rather than
        # keeping him in the queue.  If we're ever at a place where
        # there's only one player in the queue, that player wins.
        
        # This means we're actually looking for "index of a number,
        # which is larger than all of the K numbers immediately after it".
        # This allows an O(N) solution.

        winning_index = None
        winning_skill = None
        winning_streak = 0
        for index, skill in enumerate(skills):
            # print(f'[{winning_index}]{winning_skill}:{winning_streak} [{index}]{skill}')
            if winning_index is None:
                # print(f'  Start!')
                winning_index = index
                winning_skill = skill
                winning_streak = 0
                continue
            if winning_skill < skill:
                # print(f'  Challenger wins!')
                winning_index = index
                winning_skill = skill
                winning_streak = 1
            else:
                winning_streak += 1
                # print(f'  Streak continues: {winning_streak}')

            if winning_streak >= k:
                # print(f'    WINNER!')
                return winning_index
        
        # print(f'  Ran out of players!')
        return winning_index

# NOTE: Runtime 812 ms Beats 76.44%
# NOTE: Memory 31.34 MB Beats 32.93%
