
        def pattern_without_value(pattern: List[int], value: int) -> List[int]:
            assert value in pattern
            index = pattern.index(value)
            return pattern[:index] + pattern[index + 1:]

        # GENERATOR
        def all_permutations_size_K_gen(pattern: List[int], k: int) -> List[List[int]]:
            if k == 0:
                yield ()
                return

            for D in sorted(set(pattern)):
                remainder = pattern_without_value(pattern, D)
                # print(f'  {pattern=}: {D} + {remainder}')
                for value in all_permutations_size_K(remainder, k - 1):
                    yield (D,) + value
            return

        # may be cached
        def all_permutations_size_K(pattern: List[int], k: int) -> List[List[int]]:
            return tuple(all_permutations_size_K_gen(pattern, k))


