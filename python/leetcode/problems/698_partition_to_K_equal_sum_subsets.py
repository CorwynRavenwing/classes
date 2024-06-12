class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        def use_numbers(method: List[int], numbers_available: List[int]) -> List[int]:
            retval = numbers_available.copy()
            for M in method:
                if M in retval:
                    retval.remove(M)
                else:
                    # print(f'USE(): missing {M}')
                    return None
            return retval

        total_sum = sum(nums)
        print(f'{total_sum} % {k} = {total_sum % k}')
        if total_sum % k != 0:
            return False
        sum_each = total_sum // k
        print(f'{total_sum} -> {sum_each}')

        nums.sort()
        if nums[-1] > sum_each:
            print(f'{nums[-1]} > {sum_each}')
            return False

        # we borrow some code from #473 "matchsticks"

        reachable_numbers = {(0, ())}   # a list of no numbers sums to 0
        # print(f'reachable numbers:\n  {reachable_numbers}')
        for N in nums:
            # print(f'{N=}')
            new_reachable = set([
                (RN + N, combo + (N,))
                for (RN, combo) in reachable_numbers
                if RN + N <= sum_each
            ])
            # print(f'  nr={new_reachable}')
            reachable_numbers |= new_reachable  # union operator
        # print(f'reachable: {reachable_numbers}')
        sum_each_methods = [
            combo
            for (RN, combo) in reachable_numbers
            if RN == sum_each
        ]
        print(f'ways of getting {sum_each}: {sum_each_methods}')

        if not sum_each_methods:
            print(f'No way to do it!')
            return False

        to_check = [
            (0, [], nums)
        ]
        while to_check:
            check = to_check.pop(0)
            print(f'{check=}')
            (lowest_index, groups_so_far, numbers_available) = check
            if len(groups_so_far) == k:
                if not numbers_available:
                    print(f'  SUCCESS: {groups_so_far}')
                    return True
            if not numbers_available:
                print(f'  Out of numbers')
                continue
            for index, method in enumerate(sum_each_methods):
                if index < lowest_index:
                    # print(f'    skip: {index} < {lowest_index}')
                    continue
                numbers_left = use_numbers(method, numbers_available)
                if numbers_left is None:
                    # print(f'    skip: missing some numbers')
                    continue
                print(f'  method[{index}]: {method}')
                to_check.append(
                    (index, groups_so_far + [method], numbers_left)
                )

        print(f'ran out of possible answers')
        return False

