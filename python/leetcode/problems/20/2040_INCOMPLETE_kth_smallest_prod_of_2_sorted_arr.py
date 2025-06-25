class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        # def all_products_sorted_naive(nums1: List[int], nums2: List[int]) -> List[int]:
        #     all_products = [
        #         A * B
        #         for A in nums1
        #         for B in nums2
        #     ]
        #     return tuple(sorted(all_products))

        def all_products_sorted_gen(A: List[int], B: List[int]) -> List[int]:
            # output is a GENERATOR, but input must be a TUPLE
            # print(f'APSG({A},{B}):')
            if not A or not B:
                return []
            A_index = 0
            A_value = A[A_index]
            queue = [
                (
                    A_value * B_value,
                    B_value,
                    A_index,
                )
                for B_value in B
            ]
            # print(f'  {queue=}')
            while queue:
                # print(f'  DEBUG: {queue=}')
                data = queue.pop(0)
                (product, B_value, A_index) = data
                # print(f'    {product} = {B_value} * A[{A_index}]')
                yield product

                # now, create the next set of values
                A_index += 1
                try:
                    A_value = A[A_index]
                except IndexError:
                    # print(f'    A value out of range')
                    continue
                product = A_value * B_value
                data = (product, B_value, A_index)
                insort(queue, data)
            return

        # def all_products_sorted_tuple(nums1: List[int], nums2: List[int]) -> List[int]:
        #     return tuple(all_products_sorted_gen(nums1, nums2))

        # def all_products_sorted_TEST(nums1: List[int], nums2: List[int]) -> bool:
        #     A = all_products_sorted_tuple(nums1, nums2)
        #     B = all_products_sorted_naive(nums1, nums2)
        #     print(f'all_products_sorted_TEST():')
        #     print(f'    {nums1=}')
        #     print(f'    {nums2=}')
        #     passed = (A == B)
        #     if passed:
        #         print(f'  pass: answer={A}')
        #     else:
        #         print(f'  FAIL:')
        #         print(f'    check: {A}')
        #         print(f'    naive: {B}')
        #     return passed
        
        # all_products_sorted_TEST([1,2,3,], [3,4,5,])
        # all_products_sorted_TEST([2,3,5,], [7,11,13,])
        # all_products_sorted_TEST([1,2,4,], [1,2,4,])

        def filter_neg_zero_pos(nums: List[int]) -> Tuple[List[int],List[int],List[int]]:
            neg = tuple(filter(lambda x: x < 0, nums))
            zero = tuple(filter(lambda x: x == 0, nums))
            pos = tuple(filter(lambda x: x > 0, nums))
            return [neg, zero, pos]
        
        def negative_list_sorted(nums: List[int]) -> List[int]:
            negative_list = [
                -N
                for N in nums
            ]
            return tuple(sorted(negative_list))

        # print(f'TEST: {filter_neg_zero_pos([-69, -42, -13, 0, 0, 99, 420, 1040])=}')

        def listMerge(list1: List[int], list2: List[int]) -> List[int]:
            # print(f'listMerge():')
            A_iter = iter(list1)
            B_iter = iter(list2)
            # returns a GENERATOR.  May NOT be cached.
            A = next(A_iter, None)
            B = next(B_iter, None)
            # print(f'  {A=} {B=}')
            
            while A is not None and B is not None:
                if A < B:
                    yield A
                    # print(f'USE A: {A} < {B}')
                    A = next(A_iter, None)
                else:
                    yield B
                    # print(f'USE B: {A} > {B}')
                    B = next(B_iter, None)
            # print(f'Loop exited:')
            # print(f'  {A=} {B=}')

            while A is not None:
                yield A
                # print(f'USE A: {A} not empty')
                A = next(A_iter, None)
            while B is not None:
                yield B
                # print(f'USE B: {B} not empty')
                B = next(B_iter, None)

            return

        # print(f'TEST: {tuple(listMerge([1, 2, 3, 4, 5],[0, 2, 4, 6, 8]))=}')

        def Kth_value_from_generator(k: int, gen: List[int]) -> int:
            # NOTE: returns the K-th (1-based) entry, not gen[k] (0-based)
            A_iter = iter(gen)
            # print(f'{k}: seek')
            while k:
                A = next(A_iter, None)
                k -= 1
                # print(f'{k}: {A}')
            return A
        
        # print(f'TEST: {Kth_value_from_generator(3, [9,0,2,1,0])=}')

        # STEP 0: separate incoming numbers by positive, negative, zero:

        (neg1, zero1, pos1) = filter_neg_zero_pos(nums1)
        (neg2, zero2, pos2) = filter_neg_zero_pos(nums2)

        nums1_count = len(nums1)
        nums2_count = len(nums2)

        neg1_count = len(neg1)
        zero1_count = len(zero1)
        pos1_count = len(pos1)

        neg2_count = len(neg2)
        zero2_count = len(zero2)
        pos2_count = len(pos2)

        print(f'Counts: {nums1_count}({neg1_count}/{zero1_count}/{pos1_count}) {nums2_count}({neg2_count}/{zero2_count}/{pos2_count})')

        # STEP 1: negative products

        negative_product_count = sum([
            (neg1_count * pos2_count),
            (neg2_count * pos1_count),
        ])
        print(f'  {negative_product_count=}')
        if negative_product_count < k:
            k -= negative_product_count
            print(f'    SKIP.  new {k=}')
        else:
            k = negative_product_count + 1 - k
            print(f'    REVERSE: new {k=}')
            neg1_inverse = negative_list_sorted(neg1)
            neg2_inverse = negative_list_sorted(neg2)
            negXpos_gen = all_products_sorted_gen(neg1_inverse, pos2)
            posXneg_gen = all_products_sorted_gen(pos1, neg2_inverse)
            negative_gen = listMerge(
                negXpos_gen,
                posXneg_gen
            )
            answer = Kth_value_from_generator(
                k,
                negative_gen
            )
            answer = -answer    # because it's negative
            return answer

        # STEP 2: zero products

        zero_product_count = sum([
            (zero1_count * nums2_count),
            (zero2_count * nums1_count),
            -(zero1_count * zero2_count),   # which is otherwize counted twice above
        ])
        print(f'  {zero_product_count=}')
        if zero_product_count < k:
            k -= zero_product_count
            print(f'    SKIP.  new {k=}')
        else:
            return 0

        # STEP 3: positive products

        positive_product_count = sum([
            (neg1_count * neg2_count),
            (pos1_count * pos2_count),
        ])
        print(f'  {positive_product_count=}')
        if positive_product_count < k:
            k -= positive_product_count
            print(f'    SKIP.  new {k=}')
        else:
            neg1_inverse = negative_list_sorted(neg1)
            neg2_inverse = negative_list_sorted(neg2)
            negXneg_gen = all_products_sorted_gen(neg1_inverse, neg2_inverse)
            posXpos_gen = all_products_sorted_gen(pos1, pos2)
            positive_gen = listMerge(
                negXneg_gen,
                posXpos_gen
            )
            answer = Kth_value_from_generator(
                k,
                positive_gen
            )
            return answer
        
        print(f'  ERROR: answer is neither positive, zero, or negative')
        return -99999

# NOTE: Acceptance Rate 31.1% (HARD)

# NOTE: correct, but gives Time Limit Exceeded for large inputs
