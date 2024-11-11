class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:

        def parentInNormalTree(label: int) -> int:
            return label // 2
        
        def pathToRootInNormalTree(label:int) -> List[int]:
            answer = [label]
            while label > 1:
                label = parentInNormalTree(label)
                answer.append(label)
            return answer
        
        def zigzagLabel(label: int) -> int:
            # given a label, give the reflection in zigzag fashion
            # e.g. 9 -> 14
            level = len(f'{label:b}')
            # all 3-digit binary numbers are on level 3
            N = 1 << (level - 1)
            # e.g. "8" on level [8 .. 15]

            # each label is in [N..2N-1]
            # and its reflected number is arrived at by:
            # . subtract N: [0..N-1]
            # . subtract from N-1: [N-1..0]
            # . add N to this: [2N-1..0]
            # = (N + (N-1 - (label - N)))
            # = (3N-1) - label
            return 3 * N - 1 - label

        def zigzagEveryOtherLevel(path: List[int]) -> List[int]:
            return [
                (
                    value
                    if index % 2 == 0
                    else
                    zigzagLabel(value)
                )
                for index, value in enumerate(path)
            ]

        normal_path = pathToRootInNormalTree(label)
        zigzag_path = zigzagEveryOtherLevel(
            normal_path
        )
        return tuple(reversed(zigzag_path))

# NOTE: Accepted on second Run (first was invalid return type)
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 16.62 MB Beats 30.47%
