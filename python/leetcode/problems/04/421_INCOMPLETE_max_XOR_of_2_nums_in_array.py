class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:

        # SHORTCUT: each num is a collection of bits;
        # the maximum XOR will be something with the
        # highest bit set, crossed with something *without*
        # that bit set, if any such pairs exist.
        # Otherwise, ignore that bit and repeat the question.
        Max = max(nums)
        bMax = f'{Max:b}'
        bitlen = len(bMax)
        print(f'{Max=} {bMax=} {bitlen=}')
        bitsets = [
            tuple(map(int, f'{N:0{bitlen}b}'))
            for N in nums
        ]
        # print(f'{bitsets=}')

        # input: a list of bitsets
        # output: a tuple of two (lists of bitsets)
        def split_on_high_bit(bitsets: List[List[int]]) -> List[List[List[int]]]:
            haves = [
                BS
                for BS in bitsets
                if BS[0] == 1
            ]
            haveNots = [
                BS
                for BS in bitsets
                if BS[0] == 0
            ]
            return (haves, haveNots)
        
        def trim_one_high_bit(bitset: List[int]) -> List[int]:
            return bitset[1:]
        
        def trim_all_high_bits(bitsets: List[List[int]]) -> List[List[int]]:
            answer = [
                trim_one_high_bit(BS)
                for BS in bitsets
            ]
            return [
                BS
                for BS in answer
                if len(BS)
            ]
        
        def bestFit(primary: List[int], bitsets: List[List[int]]) -> List[int]:
            print(f'bestFit({primary},{len(bitsets)}):')
            if len(primary) == 0:
                return []
            if len(bitsets) == 1:
                secondary = bitsets[0]
                answerBits = [
                    A ^ B
                    for (A, B) in zip(primary, secondary)
                ]
                return answerBits
            answerBits = []
            primary_is_a_have = (primary[0] == 1)
            print(f'  {primary_is_a_have=}')
            (haves, haveNots) = split_on_high_bit(bitsets)
            print(f'  {len(haves)=}')
            print(f'  {len(haveNots)=}')
            if primary_is_a_have:
                if haveNots:
                    matches = haveNots
                    answerBits.append(1)    # 1 ^ 0
                    # print(f'  pick haveNots: {answerBits=} {matches=}')
                else:
                    matches = haves
                    answerBits.append(0)    # 1 ^ 1 === 0
                    # print(f'  no haveNots:   {answerBits=} {matches=}')
            else:
                if haves:
                    matches = haves
                    answerBits.append(1)    # 0 ^ 1
                    # print(f'  pick haves:    {answerBits=} {matches=}')
                else:
                    matches = haveNots
                    answerBits.append(0)    # 0 ^ 0
                    # print(f'  no haves:      {answerBits=} {matches=}')
            primary = trim_one_high_bit(primary)
            matches = trim_all_high_bits(matches)
            return answerBits + bestFit(primary, matches)

        answers = []
        while bitsets:
            # print(f'Loop: {bitsets=}')
            (haves, haveNots) = split_on_high_bit(bitsets)

            if (haves) and (haveNots):
                for have in haves:
                    answers.append(bestFit(have, haveNots))
                break
            else:
                # either all haves or all haveNots
                bitsets = trim_all_high_bits(bitsets)
                continue
        
        print(f'{answers=}')
        binaries = [
            ''.join(map(str, A))
            for A in answers
        ]
        print(f'{binaries=}')
        numbers = [
            int(B, 2)
            for B in binaries
        ]
        print(f'{numbers=}')

        # because i may equal j, array [X] has an answer of X^X === 0
        return max(numbers, default=0)

# NOTE: Time Limit Exceeded for large inputs
