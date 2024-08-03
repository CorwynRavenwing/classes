    def alternating(list1: List[int], list2: List[int]) -> List[int]:
        retval = list([
            item
            for pair in zip(list1, list2 + [None])
            for item in pair
        ])
        if retval[-1] is None:
            del retval[-1]
        return retval

