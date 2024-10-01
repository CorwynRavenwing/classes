class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:

        byHeightAscThenCountDesc = lambda x: (x[0], -x[1])
        people.sort(
            key=byHeightAscThenCountDesc
        )
        queue = [None] * len(people)

        for person in people:
            # print(f'{queue=}')
            (height, inFront) = person
            position = inFront + 1
            print(f'put {person=} in position #{position}')
            index = 0
            while position:
                if queue[index] is None:
                    position -= 1
                index += 1
            index -= 1
            queue[index] = person
        # print(f'{queue=}')
        return queue

# NOTE: Accepted on second Submit (first was Output Exceeded)
# NOTE: Runtime 233 ms Beats 18.37%
# NOTE: Memory 17.20 MB Beats 19.64%
