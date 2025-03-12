class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        
        # we borrow some code from #3306:

        vowels = 'aeiou'
        is_vowel = lambda x: (x in vowels)
        all_vowels = set(vowels)
        CONSONANT = "Z"
        
        word = ''.join([
            (
                char
                if is_vowel(char)
                else CONSONANT
            )
            for char in word
        ])
        # print(f'{word=}')

        letter_indexes = {
            letter: [
                (1 if char == letter else 0)
                for char in word
            ]
            for letter in vowels + CONSONANT
        }
        # print(f'{letter_indexes=}')

        ACC = lambda LIST: (0,) + tuple(accumulate(LIST))
        letter_count = {
            letter: ACC(indexes_list)
            for letter, indexes_list in letter_indexes.items()
        }
        # print(f'{letter_count=}')

        def countSubstringsAtLeastK(k: int) -> int:
            # print(f'C_S_GE_K({k}):')

            def has_all_vowels(vowel_counter: Counter) -> bool:
                nonzero_vowels = +vowel_counter
                current_vowels = set(nonzero_vowels.keys())
                return (current_vowels == all_vowels)
            
            missing_any_vowels = lambda COUNTER: (not has_all_vowels(COUNTER))

            def MinRWithEnoughLetters(Leftmost: int) -> int:
                # print(f'\nMinR({Leftmost}):\n')

                def hasEnoughLetters(Rightmost: int) -> bool:
                    # print(f'  Enough({Rightmost})')
                    # frag = word[Leftmost:Rightmost]
                    # counts = Counter(frag)
                    counts = Counter({
                        letter: partialSum[Rightmost + 1] - partialSum[Leftmost]
                        for letter, partialSum in letter_count.items()
                    })
                    # print(f'  -> {counts=}')
                    if counts[CONSONANT] < k:
                        # print(f'  (false)')
                        return False
                    counts[CONSONANT] = 0
                    if missing_any_vowels(counts):
                        # print(f'  (false)')
                        return False
                    # print(f'  (TRUE)')
                    return True

                L = Leftmost
                left = hasEnoughLetters(L)
                if left:
                    # print(f'Strange, {L=} is true')
                    return L
                R = len(word) - 1
                right = hasEnoughLetters(R)
                if not right:
                    # print(f'Strange, {R=} is false')
                    return None
                # print(f'[{L},{R}] ({left},{right})')
                while L + 1 < R:
                    M = (L + R) // 2
                    mid = hasEnoughLetters(M)
                    # print(f'[{L},{M},{R}] ({left},{mid},{right})')
                    if mid:
                        # print(f'  True: replace Right')
                        (R, right) = (M, mid)
                    else:
                        # print(f'  False: replace Left')
                        (L, left) = (M, mid)

                # print(f'[{L},{R}] ({left},{right})')
                # R is now the lowest possible True value
                return R

            # SHOW = lambda COUNT: ''.join(sorted(set((+COUNT).keys())))

            answer = 0

            for L in range(len(word)):
                R = MinRWithEnoughLetters(L)

                # print(f'[{L},{R}]: "{char}" C={consonant_count}/{k} V={SHOW(vowel_counter)}')
                # print(f'*[{L},{R}]:')
                if R is not None:
                    delta = len(word) - R
                    answer += delta
                    # print(f'  {answer=} (+{delta})')
                L += 1

            return answer

        at_least_k = countSubstringsAtLeastK(k)
        at_least_k_plus_1 = countSubstringsAtLeastK(k + 1)
        exactly_k = at_least_k - at_least_k_plus_1

        print(f'{exactly_k=} = {at_least_k=} - {at_least_k_plus_1=}')

        return exactly_k

# NOTE: re-used entire code from prior version
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 519 ms Beats 15.39%
# NOTE: Memory 18.47 MB Beats 25.13%
