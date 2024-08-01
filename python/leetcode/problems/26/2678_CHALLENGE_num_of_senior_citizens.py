class Solution:
    def countSeniors(self, details: List[str]) -> int:

        seniors = 0
        for D in details:
            phone = D[:10]
            gender = D[10]
            age = D[11:13]
            seat = D[13:]
            print(f'{phone} "{gender}" {age=} "{seat}"')
            if int(age) > 60:
                print(f'  SENIOR')
                seniors += 1
        return seniors
# NOTE: accepted first time in "run" mode
# NOTE: accepted first time when submitted
# NOTE: Runtime 43 ms Beats 78.00%
# NOTE: Memory 16.70 MB Beats 7.17%
