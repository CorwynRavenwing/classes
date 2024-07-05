class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:

        samples = [
            [N, C]
            for N, C in enumerate(count)
            if C != 0
        ]
        print(f'{samples=}')

        (minimum, minCount) = samples[0]

        (maximum, maxCount) = samples[-1]

        sample_total = sum([
            N * C
            for (N, C) in samples
        ])
        sample_count_list = [
            C
            for (N, C) in samples
        ]
        sample_count = sum(sample_count_list)
        highest_count = max(sample_count_list)

        mean = sample_total / sample_count
        print(f'mean = {sample_total} / {sample_count}')

        modulo = sample_count % 2               # 0 for even, 1 for odd
        center = sample_count // 2 + modulo     # 4 -> 2, 5 -> 3, 6 -> 3
        print(f'Pick sample #{center}{f"+ {center+1}" if modulo == 0 else ""}')
        median_candidates = []
        for (N, C) in samples:
            print(f'sample {(N, C)} {center=}:')
            if center > C:
                print(f'{center} > {C}, skip')
                center -= C
                continue
            else:
                print(f'  pick {N}')
                median_candidates.append(N)
                if modulo == 1:
                    print(f'  odd: break {median_candidates}')
                    break
                elif len(median_candidates) >= 2:
                    print(f'  two candidates: break {median_candidates}')
                    break
                else:
                    print(f'  even: pick another {median_candidates}')
                    center += 1
                    if center > C:
                        print(f'{center} > {C}, skip')
                        center -= C
                        continue
                    else:
                        print(f'  pick {N}')
                        median_candidates.append(N)
                        print(f'  second candidate: break {median_candidates}')
                        break
        median = sum(median_candidates) / len(median_candidates)

        mode_candidates = [
            N
            for (N, C) in samples
            if C == highest_count
        ]
        mode = (
            mode_candidates[0]
            if len(mode_candidates) == 1
            else 'error: multiple values tied for mode'
        )

        return [minimum, maximum, mean, median, mode]
# NOTE: 46 ms; Beats 62.43%
