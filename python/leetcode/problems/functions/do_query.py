
        def doQuery(Q: List[int]) -> int:
            print(f'{Q=}')
            return 42

        return [
            doQuery(Q)
            for Q in queries
        ]

