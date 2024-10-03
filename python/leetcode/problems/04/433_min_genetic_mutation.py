class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        if endGene not in bank:
            return -1
        
        # we borrow some code from #752:

        def geneDistance(gene1: str, gene2: str) -> int:
            return sum([
                1 if (A != B) else 0
                for A, B in zip(gene1, gene2)
            ])

        def neighborsOf(gene: str) -> List[str]:
            # here, instead of enumerating all possible changes,
            # and then checking for them in the bank, we are
            # checking the bank for legal genes with
            # a distance of 1
            neighbors = [
                gene2
                for gene2 in bank
                if geneDistance(gene, gene2) == 1
            ]
            return neighbors

        states = {startGene}
        known = set()
        answer = 0
        while states:
            print(f'{answer}: L={len(states)}')
            new_states = set()
            for gene in states:
                print(f'  {gene}', end="")
                # if gene in deadends:
                #     print(f' -> DEAD END')
                #     continue
                if gene in known:
                    print(f' -> duplicate')
                    continue
                if gene == endGene:
                    print(f' -> YES')
                    return answer
                known.add(gene)
                neighbors = neighborsOf(gene)
                for N in neighbors:
                    new_states.add(N)
                # print(f' -> {" ".join(neighbors)}')
            states = new_states
            answer += 1

        print(f'FAILURE')
        return -1

# NOTE: Re-used all the code from prior version, with minor changes
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 22 ms Beats 99.05%
# NOTE: Memory 16.46 MB Beats 83.14%
