class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:

        coordinates = tuple(sorted(map(tuple, coordinates)))
        counts = Counter(coordinates)
        # print(f'{counts=}')

        # okay, so we define (1) A as (x1 XOR x2) and (2) B as (y1 XOR y2).
        # which means we're looking for distance = (3) A + B = k.
        # since XOR is its own inverse, equation 1 means (4) x2 = (A XOR x1)
        # and eq. 2 means (5) y2 = B XOR y1; also, eq. 3 means (6) B = k - A.
        # substitute eq. 6 into eq. 5 and you get (7) y2 = (k - A) XOR y1.
        # So, equation 4 gives you x2 from x1, given a particular A,
        # and equation 7 gives you y2 from y1, given a value for A as well.
        # This means we can loop through possible values of A, and determine
        # the proper (x2, y2) for each (x1, y1) pair.
        # And A can only take on a value <= k, and k can only be 0 .. 100.
        # (I had thought that the Xs and Ys can be up to 20 bits, but the
        # k maximum puts a hard cap on A)

        answer = 0
        for P1 in coordinates:
            (x1, y1) = P1
            # print(f'{(x1,y1)=}')
            counts[P1] -= 1
            if not counts[P1]:
                del counts[P1]
            # print(f'  {counts=}')
            for A in range(k+1):
                x2 = (A ^ x1)       # "^" == XOR
                y2 = (k - A) ^ y1
                # print(f'  {A=} {(x2,y2)=}')
                if (x2,y2) in counts:
                    # print(f'  {A=} {(x2,y2)}: YES (+{counts[(x2,y2)]})')
                    # print(f'    YES (+{counts[(x2,y2)]})')
                    answer += counts[(x2,y2)]
                # else:
                #     # print(f'    NO')

        return answer
# NOTE: Runtime 2761 ms Beats 80.56%
# NOTE: Memory 36.29 MB Beats 59.72%
