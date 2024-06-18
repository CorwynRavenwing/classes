class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def reversed_str(s: str) -> str:
            return ''.join(
                reversed(s)
            )

        def is_palindrome(s: str) -> bool:
            return reversed_str(s) == s
        
        def all_positions(ch: str, s: str) -> list:
            positions = []
            start_pos = 0
            while start_pos != -1:
                next_pos = s.find(ch, start_pos)
                if next_pos == -1:
                    start_pos = next_pos
                    continue
                else:
                    positions.append(next_pos)
                    start_pos = next_pos + 1
            return positions

        max_string = ''
        max_len = len(max_string)

        letters = list(sorted(list(set(s))))
        print(f"#{letters=}")
        for letter in letters:
            positions = all_positions(letter, s)
            # print(f"#  {letter=} {positions=}")
            for i, pos1 in enumerate(positions):
                for j, pos2 in enumerate(positions):
                    if i > j:
                        # must be left to right
                        continue
                    # print(f"#    {i=} {j=} {pos1=} {pos2=}")
                    test = s[pos1:pos2+1]
                    len_test = len(test)
                    # print(f"#      {len_test=} {max_len=}")
                    if len_test <= max_len:
                        # print("#      SHORT")
                        continue
                    if is_palindrome(test):
                        # print(f"#      PASS: {test}")
                        max_string = test
                        max_len = len_test
                    else:
                        # print("#      FAIL")
                        continue

        return max_string

