
        def sum_not_none(L: list) -> int:
            while None in L:
                L.remove(None)
            return sum(L)

