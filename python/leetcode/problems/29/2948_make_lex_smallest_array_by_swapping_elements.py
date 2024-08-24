class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:

        # SHORTCUT 1: If I can swap A and B, and B and C, then I can swap A and C
        # therefore I only care about interconnected groups that are swappable

        # SHORTCUT 2: in a sorted list, all swappable groups will be contiguous

        sorted_nums = sorted(nums)

        swappable_groups = {}
        group_leader = None
        prior = None
        for N in sorted_nums:
            if group_leader is None:
                group_leader = N
                assert group_leader not in swappable_groups
                swappable_groups[group_leader] = [N]
                prior = N
                # print(f'First group led by {group_leader}')
            elif N - prior <= limit:
                # print(f'  Add {N} to group #{group_leader}')
                swappable_groups[group_leader].append(N)    # already sorted
                prior = N
            else:
                group_leader = N
                assert group_leader not in swappable_groups
                swappable_groups[group_leader] = [N]
                prior = N
                # print(f'New group led by {group_leader}')
        # print(f'{swappable_groups=}')

        my_group = {
            # duplicate members will always be in the same group
            # this dict comprehension deals properly with such dups
            me: group
            for group, members in swappable_groups.items()
            for me in members
        }
        # print(f'{my_group=}')

        group_ids = [
            # for each N, find what group it belongs to
            my_group[N]
            for N in nums
        ]
        # print(f'{group_ids=}')

        answer = [
            # grab the list of members of that group
            # pop (take and delete) the first (=== min) member available
            swappable_groups[G].pop(0)
            for G in group_ids
        ]

        return answer
# NOTE: Runtime 2535 ms Beats 5.41%
# NOTE: Memory 49.60 MB Beats 38.74%
