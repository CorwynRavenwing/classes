
        def centerObject(thing: List[any]) -> any:
            if thing is None:
                return None
            Len = len(thing)
            even = (Len % 2 == 0)
            if even:
                return None
            Half = Len // 2
            print(f'{Len=} {even=} {Half=}')
            centerObj = thing[Half]
            return centerObj


