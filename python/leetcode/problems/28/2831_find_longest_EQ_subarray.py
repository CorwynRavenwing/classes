class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:

        indexesByValue = {}
        for index, value in enumerate(nums):
            indexesByValue.setdefault(value, [])
            indexesByValue[value].append(index)
        # print(f'{indexesByValue=}')

        maxValue = 1    # any one value [X] is an "equal subarray" of length=1
        for value, indexes in indexesByValue.items():
            print(f'{value}: {indexes=}')
            # print(f'{value}: {len(indexes)=}')
            # SHORTCUT 1:
            # to_delete = (indexJ - indexI) - (j - i)
            # === indexJ - indexI - j + i
            # === indexJ - j - indexI + i
            # === (indexJ - j) - (indexI - i)
            # which is two similar pieces only dependent on one variable apiece
            indexX_minus_X_comma_X = [
                (indexX - X, X)
                for X, indexX in enumerate(indexes)
            ]
            print(f'{indexX_minus_X_comma_X=}')
            for indexI_minus_I, i in indexX_minus_X_comma_X:
                # SHORTCUT 2:
                # indexJ_minus_J - indexI_minus_I <= k
                # --> indexJ_minus_J <= k + indexI_minus_I
                max_indexJ_minus_J = k + indexI_minus_I
                max_j = bisect_right(indexX_minus_X_comma_X, (max_indexJ_minus_J, 0), i)
                for indexJ_minus_J, j in indexX_minus_X_comma_X[i+1:max_j]:
                    if i >= j:
                        print(f'  TOO SMALL {i} >= {j}')
                        continue
                    this_span = j - i + 1
                    if this_span <= maxValue:
                        # will not help
                        continue
                    print(f'  [{i},{j}] ({indexI_minus_I},{indexJ_minus_J}) {this_span=}')
                    to_delete = (indexJ_minus_J - indexI_minus_I)
                    print(f'    {to_delete=} {k=}')
                    if to_delete > k:
                        # too many other values to delete them all
                        print(f'  TOO MANY TO DELETE!')
                        break
                        # if there's too many deletions in A..B,
                        # there will be more in I..J..J+1
                        # so start over with new I
                    maxValue = max(maxValue, this_span)
                    # print(f'      possible answer {j - i + 1}')

        return maxValue
# NOTE: Time limit Exceeded for large inputs
# NOTE: This is after following the "hints" exactly, and then
#       making the system much more efficient: it still gives TLE.
