class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:

        milestone_by_project = [
            [milestone, project]
            for project, milestone in enumerate(milestones)
        ]
        milestone_by_project.sort(reverse=True)

        projects = []
        while milestone_by_project:
            # print(f'{projects=} {milestone_by_project=}')
            pNum = 0
            MS = milestone_by_project[pNum]
            if projects and projects[-1] == MS[1]:
                if len(milestone_by_project) > 1:
                    pNum = 1
                    MS = milestone_by_project[pNum]
                else:
                    print(f'cannot repeat task #{MS[1]}; no other task available')
                    break
            projects.append(MS[1])
            MS[0] -= 1
            if not MS[0]:
                print(f'Project #{MS[1]} complete')
                del milestone_by_project[pNum]
            milestone_by_project.sort(reverse=True)

        print(f'{projects=} {milestone_by_project=}')
        return len(projects)
# NOTE: Works, but Time Limit Exceeded for ludicrously large inputs
