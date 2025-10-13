class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        
        mod = 10 ** 9 + 7

        def add_binary(value, prior_binary, prior_setbits) -> Tuple[List[int],int]:
            # return value === (
            #   (binary sequence of sum, in reverse order),
            #   number_of_set_bits
            # )
            this_binary = list(prior_binary)
            this_setbits = prior_setbits
            while value is not None:
                # print(f'{value=} {this_setbits=} {this_binary=}')
                try:
                    _ = this_binary[value]
                except IndexError:
                    this_binary.append(0)
                    continue
                
                if this_binary[value] == 0:
                    this_binary[value] = 1
                    this_setbits += 1
                    value = None
                    break
                else:
                    this_binary[value] = 0
                    this_setbits -= 1
                    value += 1
                    continue
                raise Exception('write me')
        
            # print(f'value=- {this_setbits=} {this_binary=}')
            return (tuple(this_binary), this_setbits)
        
        # test
        # print(f'{add_binary(0, (1,1,1,1,1), 5)=}')
        # print(f'{add_binary(2, (1,1,1,1,1), 5)=}')
        # print(f'{add_binary(0, (1,1,0,1,1), 4)=}')

        def sequence_gen(m: int, n: int) -> Tuple[List[int],List[int],int]:
            # n === nums.length === max value (non-inclusive)
            #   for each seq member
            # return value === (
            #   (values of sequence),
            #   (binary sequence of sum, in reverse order),
            #   number_of_set_bits
            # )
            if m == 0:
                yield ((), (), 0)
                return
            for (prior_seq, prior_binary, prior_setbits) in sequence(m - 1, n):
                for value in range(n):
                    this_seq = prior_seq + (value,)
                    (
                        this_binary,
                        this_setbits
                    ) = add_binary(value, prior_binary, prior_setbits)
                    yield (
                        this_seq,
                        this_binary,
                        this_setbits
                    )
            return
        
        @cache
        def sequence(m: int, n: int) -> Tuple[List[int],List[int],int]:
            return tuple(sequence_gen(m, n))
        
        # print(f'test: {sequence(m, len(nums))=}')

        def magical_sequences_gen() -> List[List[int]]:
            # nonlocal m
            # nonlocal k
            # nonlocal nums
            for (seq, binary, setbits) in sequence(m, len(nums)):
                if setbits == k:
                    yield seq
            return
        
        @cache
        def magical_sequences() -> List[List[int]]:
            return tuple(magical_sequences_gen())

        # print(f'test: {magical_sequences()=}')

        @cache
        def array_product_mod(seq: List[int]) -> int:
            # nonlocal mod
            # nonlocal nums
            print(f'APM({seq})')
            if seq == ():
                # print(f'APM({seq}): 0 1')
                return 1
            last = seq[-1]
            rest = seq[:-1]
            answer = array_product_mod(rest)
            # print(f'APM({seq}): A {answer}')
            answer *= nums[last]
            # print(f'APM({seq}): B {answer}')
            answer %= mod
            # print(f'APM({seq}): C {answer}')
            return answer

        answer = 0
        for seq in magical_sequences():
            seq = tuple(sorted(seq))
            # print(f'{seq=}')
            APM = array_product_mod(seq)
            # print(f'{seq=} D {answer}')
            answer += APM
            # print(f'{seq=} E {answer}')
            answer %= mod
            print(f'{seq=} {answer}')

        return answer % mod

# NOTE: Acceptance Rate 36.4% (HARD)

# NOTE: TLE; should use combinatorics
