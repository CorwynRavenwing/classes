        
        def set_bits(i: int) -> int:
            binary = f'{i:b}'
            digits = tuple(map(int, binary))
            return sum(digits)

