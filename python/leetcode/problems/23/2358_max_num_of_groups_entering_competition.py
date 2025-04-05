class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        
        grades.sort()
        L = 0
        groups = 0
        group_size = 1
        this_group_size = group_size
        this_group_total = 0
        prior_group_size = 0
        prior_group_total = 0
        while L < len(grades):
            R = L + group_size
            frag = grades[L:R]
            this_group_size = len(frag)
            this_group_total = sum(frag)
            print(f'{groups + 1}: [{L}:{R}] {frag} {this_group_size} ({this_group_total})')
            if this_group_size <= prior_group_size:
                print(f'  too few people')
                break
            if this_group_total <= prior_group_total:
                print(f'  too low of scores')
                break
            groups += 1
            group_size += 1
            L = R
            prior_group_size = this_group_size
            prior_group_total = this_group_total
        
        return groups

# NOTE: Accepted on third Run (fencepost errors)
# NOTE: Accepted on first Submit
# NOTE: Runtime 82 ms Beats 10.95%
# NOTE: Memory 28.05 MB Beats 22.38%
