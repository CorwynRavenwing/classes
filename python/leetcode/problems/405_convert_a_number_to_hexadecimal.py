class Solution:
    def toHex(self, num: int) -> str:
        
        def clean_binary(binary: List[int]) -> List[int]:
            while max(binary) >= 2:
                if binary[0] >= 2:
                    binary = [0] + binary
                index = binary.index(max(binary))
                carry = binary[index] // 2
                binary[index - 1] += carry
                binary[index] -= carry * 2
            return binary

        def int_to_binary(num: int) -> List[int]:
            assert num >= 0
            answer = [num]
            return clean_binary(answer)
        
        def binary_to_int(binary: List[int]) -> int:
            answer = 0
            for bit in binary:
                answer *= 2
                answer += bit
            return answer

        def binary_to_hex(binary: List[int]) -> str:
            heximal = ''
            while binary:
                blockBin = binary[-4:]
                binary = binary[:-4]
                blockInt = binary_to_int(blockBin)
                assert 0 <= blockInt <= 15
                blockHex = (
                    '0123456789abcdef'[blockInt]
                )
                heximal = blockHex + heximal
            return heximal
        
        def ones_complement(binary: List[int]) -> List[int]:
            bits = 8 * 4    # 'ffffffff' * bits in 'f'
            binary = [0] * (bits - len(binary)) + binary
            print(f'padded: {binary=}')
            answer = [
                1 if B == 0 else 0
                for B in binary
            ]
            return list(answer)

        def binary_add_1(binary: List[int]) -> List[int]:
            binary[-1] += 1
            return clean_binary(binary)
        
        print(f"{num=}")

        if num == 0:
            return '0'
        
        if num > 0:
            binary = int_to_binary(num)
            print(f"{binary=}")
            check = binary_to_int(binary)
            print(f"{check=}")
            assert num == check
            heximal = binary_to_hex(binary)
            print(f"{heximal=}")
            return heximal

        if num < 0:
            pos_num = -num
            pos_binary = int_to_binary(pos_num)
            print(f"{pos_binary=}")
            complement = ones_complement(pos_binary)
            print(f"{complement=}")
            binary = binary_add_1(complement)
            print(f"{binary=}")
            heximal = binary_to_hex(binary)
            print(f"{heximal=}")
            return heximal

