class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        words.sort(
            key=len
        )

        print(f'sorted {words=}')
        answer = []
        while words:
            word = words.pop(0)    # shortest one
            for W in words:
                # for each of the others
                if word in W:
                    answer.append(word)
                    break
        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 39 ms Beats 5.67%
# NOTE: Memory 17.67 MB Beats 28.23%

# NOTE: THE CHALLENGE DID NOT ACCEPT THIS ANSWER

# NOTE: re-ran and received:
# NOTE: Runtime 3 ms Beats 64.01%
# NOTE: Memory 17.67 MB Beats 28.23%
# NOTE: ... which is 10x better speed!

# NOTE: challenge still did not accept

# NOTE: re-ran a third time:
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.72 MB Beats 19.52%

# NOTE: I now note that the "challenge up-to-date" flag is set
# NOTE: although the pop-up still has not happened.
