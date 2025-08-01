
        # 3-wide version of pairwise:

        def triwise(iterable):
            a, b = tee(iterable)
            a, c = tee(iterable)
            next(b, None)
            next(c, None)
            next(c, None)
            return zip(a, b, c)

