class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        def filter_all_same(items: List[str]) -> str:
            item = items.pop()
            for next_item in items:
                if item != next_item:
                    return None
            return item

        m = list(map(list, strs))
        print(f"{m=}")
        zT = list(zip(*m))
        print(f"{zT=}")
        zL = list(map(list, zT))
        print(f"{zL=}")
        c = list(map(filter_all_same, zL))
        print(f"{c=}")
        if None in c:
            index = c.index(None)
            c = c[:index]
            print(f"{c=}")
        return ''.join(c)

