class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:

        ages.sort()
        answer = 0
        for i, X in enumerate(ages):
            Y = X / 2 + 7
            # looking for people Y < age <= X
            print(f'[{i}] {X}: {Y}')
            left_index = bisect.bisect_right(ages, Y)
            right_index = bisect.bisect_right(ages, X)
            if left_index >= right_index:
                print(f'  no possible ages')
                # e.g. 5: 9.5 < Y <= 5, which is impossible
                continue
            Xs_friends = right_index - left_index
            if left_index <= i < right_index:
                Xs_friends -= 1     # remove X himself
            print(f'  {left_index}:{right_index} ({Xs_friends})')
            answer += Xs_friends

        return answer

