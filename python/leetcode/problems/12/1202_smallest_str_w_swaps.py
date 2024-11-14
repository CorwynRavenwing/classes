class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        nodes = tuple(range(len(s)))
        NodeGroup = {
            i: i
            for i in nodes
        }
        def getGroup(i: int) -> int:
            j = NodeGroup[i]
            if i != j:
                j = getGroup(j)
                NodeGroup[i] = j
            return j

        def sameGroup(i: int, j: int) -> bool:
            return getGroup(i) == getGroup(j)

        def mergeGroups(i: int, j: int):
            i = getGroup(i)
            j = getGroup(j)
            if i != j:
                if i < j:
                    (i, j) = (j, i)     # make J the lower one
                NodeGroup[i] = j
            return

        # SHORTCUT: since we can exchange pairs any number of times,
        # all the letters reachable by any number of swaps are all
        # equivalent to one another.  The updated mergeGroups() above
        # turns any letter into the smallest equivalent letter.

        for a, b in pairs:
            print(f'pair {(a,b)=}')
            mergeGroups(a, b)

        chars_by_group = {}
        for index, C in enumerate(s):
            group = getGroup(index)
            print(f'[{index}]"{C}" -> {group}')
            chars_by_group.setdefault(group, [])
            bisect.insort(chars_by_group[group], C)
            # print(f'  :{chars_by_group[group]}')

        print()
        answer = []
        for index in range(len(s)):
            group = getGroup(index)
            C = chars_by_group[group].pop(0)
            print(f'[{index}]:{group} -> "{C}"')
            answer.append(C)

        return ''.join(answer)

# NOTE: Accepted on first Submit
# NOTE: Runtime 1268 ms Beats 5.11%
# NOTE: Memory 49.30 MB Beats 76.81%
