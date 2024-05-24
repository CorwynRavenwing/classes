class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        print(f'maxEnvelopes({len(envelopes)})')
        
        # we reuse much of the code from problem #300

        def envelope_fits_in(A, B):
            (wA, hA) = A
            (wB, hB) = B
            return (wA < wB) and (hA < hB)

        # data[i] = best number of envelopes ending at position i
        data = [None] * len(envelopes)

        # always use smallest envelopes first
        envelopes.sort(
            # sort by width, then by REVERSE height.
            # this means that anything I can fit in, is to my left
            # and we can do a bisection sort looking for fit with "<"
            key=lambda x: (x[0], -x[1])
        )
        # print(f'{envelopes=}')
        
        max_value = 0
        max_index = None
        for i, this_envelope in enumerate(envelopes):
            # print(f'{i=} {data[:i]=}')
            # print(f'  {envelopes[:i]=} {this_envelope=}')

            (W, H) = this_envelope

            max_j = bisect.bisect_right(envelopes, this_envelope, 0, i)
            # print(f'{i=} {this_envelope} insert@ {max_j}: {envelopes[max_j-1:max_j+1] if max_j else envelopes[:max_j+1]}')

            # try best-case first:
            if max_value:
                best_prior = max_value
                best_index = max_index
                prior_envelope = envelopes[best_index]
                if envelope_fits_in(prior_envelope, this_envelope):
                    # shortcut
                    answer = best_prior + 1
                    data[i] = answer
                    if max_value < answer:
                        max_value = answer
                        max_index = i
                        # print(f'NEW MAX[{i}] = {answer} (A)')
                    continue
            

            # print(f'{this_envelope=}')
            # checksums = [
            #     (E, (1 if envelope_fits_in(E, this_envelope) else 2))
            #     for E in envelopes[:max_j]
            # ]
            # print(f'{checksums=}')

            # print(f'  getting checks: {max_j=}')
            check = envelopes[:max_j]
            check.sort(
                key=lambda x: x[1]
            )
            max_j = bisect.bisect_left(check, this_envelope)
            # print(f'  getting priors: {max_j=}')
            priors = data[:max_j]

            
            
            # priors = [
            #     Dval
            #     for Dindex, Dval in enumerate(data[:max_j])
            #     if envelope_fits_in(envelopes[Dindex], this_envelope)
            # ]
            # # print(f'    {priors=}')
            best_prior = max(priors) if priors else 0
            answer = best_prior + 1
            data[i] = answer
            if max_value < answer:
                max_value = answer
                max_index = i
                # print(f'NEW MAX[{i}] = {answer} (B)')
            # print(f'    {best_prior=} {data[i]=}')
        
        # print(f'{data=}')
        # return max(data)
        # print(f'{max_index=} {max_value=}')
        return max_value

# NOTE: still timing out for large data sets

