class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:

        biggest_project = max(milestones)
        all_other_projects = sum(milestones) - biggest_project

        if biggest_project > all_other_projects:
            # start with biggest
            # alternate with anything else
            # end with biggest
            # stop
            return 2 * all_other_projects + 1
        else:
            # we can squeeze in everything
            return biggest_project + all_other_projects
# NOTE: a logical answer instead of working it out each time
# NOTE: Runtime 545 ms Beats 81.50%
# NOTE: Memory 28.12 MB Beats 75.14%
