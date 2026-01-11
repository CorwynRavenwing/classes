
        def min_not_none(L: list) -> int:
            while None in L:
                L.remove(None)
            return min(L, default=None)

