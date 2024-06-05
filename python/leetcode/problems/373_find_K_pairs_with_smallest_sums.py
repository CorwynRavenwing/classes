class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        def indexes_to_total_pair_and_indexes(indexes: Tuple[int,int]) -> Tuple[int,Tuple[int,int],Tuple[int,int]]:
            (i, j) = indexes
            try:
                pair = (nums1[i], nums2[j])
            except IndexError:
                return None
            total = sum(pair)
            return (total, pair, indexes)

        answers = []
        seen = set()
        pool = []

        def next_pair(indexes: Tuple[int,int]) -> List[Tuple[int,int]]:
            nonlocal seen
            retval = []
            seen.add(indexes)
            for listNum in [0, 1]:
                new_indexes = tuple([
                    value + (1 if i == listNum else 0)
                    for i, value in enumerate(indexes)
                ])
                if new_indexes in seen:
                    print(f'  skip {new_indexes}: seen')
                    continue
                seen.add(new_indexes)
                # print(f'GEN[{listNum}]: {indexes} -> {new_indexes}')
                retval.append(new_indexes)
            return retval
        
        def generate_pairs() -> Tuple[int,int]:
            nonlocal answers, seen, pool
            i = 0
            origin = (0,0)
            TPI = indexes_to_total_pair_and_indexes(origin)
            (total, pair, indexes) = TPI
            print(f'#{i}: {total}={pair} [{indexes}]')
            answers.append(TPI)
            ###
            for next_index in next_pair(indexes):
                next_TPI = indexes_to_total_pair_and_indexes(next_index)
                if next_TPI is None:
                    print(f'  skip {next_index}: OOB')
                    continue
                pool.append(next_TPI)
            ###
            yield pair

            while True:
                i += 1
                pool.sort()
                if not pool:
                    print(f'POOL EMPTY')
                    break
                TPI = pool.pop(0)
                (total, pair, indexes) = TPI
                print(f'#{i}: {total}={pair} [{indexes}]')
                answers.append(TPI)
                ###
                for next_index in next_pair(indexes):
                    next_TPI = indexes_to_total_pair_and_indexes(next_index)
                    if next_TPI is None:
                        print(f'  skip {next_index}: OOB')
                        continue
                    pool.append(next_TPI)
                ###
                yield pair

        pair_gen = generate_pairs()
        retval = []
        for _ in range(k):
            try:
                kth_pair = next(pair_gen)
            except StopIteration:
                print(f'  STOP')
                break
            # print(f'  {_}/{k} -> {kth_pair}')
            retval.append(kth_pair)
        # print(f'{answers=}')
        # print(f'{retval=}')
        print(f'Next few:')
        for _ in range(5):
            try:
                kth_pair = next(pair_gen)
            except StopIteration:
                print(f'  STOP')
                break
            print(f'  {_}/{5} -> {kth_pair}')
        return retval

