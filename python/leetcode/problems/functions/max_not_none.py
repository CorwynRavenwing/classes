
        def max_not_none(L: list) -> int:
            while None in L:
                L.remove(None)
            return max(L, default=None)

