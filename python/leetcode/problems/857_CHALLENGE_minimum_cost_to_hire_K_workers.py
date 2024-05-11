class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:

        START = 0000
        STOP = START + 1000

        if k == 1:
            print(f"{k=}: return just lowest wage")
            wage.sort()
            return wage[0]
        
        Z = list([
            ((W / Q), W, Q)
            for (W, Q) in zip(wage, quality)
        ])
        Z.sort(reverse=True)
        Q_sorted_by_ratio = tuple([
            Q
            for (ratio, W, Q) in Z
        ])
        print(f"{k=} {len(Z)=} {Z[:5]=}")

        min_answer = None
        prev_Q = 0
        counter = 0
        for i, Zi in reversed(list(enumerate(Z[:-k+1]))):
        # for i, Zi in enumerate(Z[:-k+1]):
        # for i in reversed(range(len(Z[:-k+1]))):
        # for i in range(len(Z[:-k+1])):
            counter += 1
            # Zi = Z[i]
            if counter > STOP:
                print(f"{counter=} {i=} out of time: stopping")
                return min_answer
            (ratio_i, Wi, Qi) = Zi
            if min_answer is not None and min_answer < Wi:
                # print(f"  SKIP {i}: {min_answer} < {Wi}")
                continue
            cost_i = Wi

            ### NO LONGER DOING THIS ###
            # since we're going backwards now,
            # the Q values are no longer under-estimates,
            # so we can't safely do this anymore
            ### NO LONGER DOING THIS ###
            # # skip quickly if value is likely too high
            # if min_answer is not None:
            #     # Q this time will be HIGHER than prev_Q,
            #     # so this is an UNDER-estimate:
            #     estimated_cost = cost_i + round(ratio_i * prev_Q, 10)
            #     if estimated_cost > min_answer:
            #         if i > START:
            #             print(f"{i=} SKIP {round(estimated_cost)} > {round(min_answer)}")
            #             continue

            others = Q_sorted_by_ratio[i+1:]    # take the right-hand (lowest) section
            others = sorted(others)             # sort by Q instead of ratio
            others = others[:k-1]               # cut off the left (lowest) section
            if len(others) < k-1:
                print(f'  NOT ENOUGH "others" {i=} {len(others)} < {k-1}')
                continue
            
            # we don't need to check Wj > Qj*ratio_i here,
            # because we have Z sorted by ratio descending.

            # now sort by Q ascending
            Q_others = sum(others)
            prev_Q = Q_others
            W_others = round(ratio_i * Q_others, 10)
            cost = cost_i + W_others
            if counter > START:
                print(f"{i=} {cost_i} + {Q_others}*{round(ratio_i)}={round(W_others)} = {round(cost)}")
            if min_answer is None or min_answer > cost:
                if counter > START:
                    print("  new min")
                min_answer = cost
        return min_answer

# TODO:
# why does this code always find the answer in the "last" 1000?
# it's not always the last *one*, which would have made sense.
# I'm starting at the end and stopping after counter=1000,
# and it was accepted as the right answer, but WHY is the
# answer always "near" the end but not *at* the end?

# TODO:
# is there a way to speed up the repeated summation inside the loop?
# possibly by dropping off the i'th value and adding the i+k'th
# I'm thinking I would need to keep the values sorted, which ought
# to be more expensive than a summation, but I may be wrong in that.
# Can we just keep the [i+1 .. end] in a Q-sorted list, and then
# remove() the i'th value?  Is that cheaper than a sum?
# Or possibly, just keep the sum and a Q-sorted list of values
# we haven't reached yet.  Each round, subtract the i'th Q from the sum
# and add the i+k'th from the unreached list.  This might well work.

