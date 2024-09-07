class Solution:
    def minAnagramLength(self, s: str) -> int:
        
        def factors_of(N: int) -> List[int]:
            answers = []
            for D in range(1, N // 2 + 1):
                if N % D == 0:
                    Q = N // D
                    if D > Q:
                        break
                    answers.append(D)
                    if Q != D:
                        answers.append(Q)
            return sorted(answers)
        
        print(f'{len(s)=}')
        for F in factors_of(len(s)):
            print(f'  {F=}')
            T = s
            spec_count = None
            accepted = True
            while T:
                chunk = T[:F]
                T = T[F:]
                print(f'    {chunk=}')
                chunk_count = Counter(chunk)
                if spec_count is None:
                    print(f'      First chunk: set as the spec')
                    spec_count = chunk_count
                    continue
                elif spec_count != chunk_count:
                    print(f'      Counts differ:\n\t\t{spec_count =}\n\t\t{chunk_count=}')
                    accepted = False
                    break
            if accepted:
                # print(f'    Accept {F=}')
                return F

        return len(s)

# NOTE: Accepted on first Submit
# NOTE: Runtime 2178 ms Beats 5.14%
# NOTE: Memory 18.10 MB Beats 26.17%
