class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        nodes = tuple(set([
            email
            for A in accounts
            for email in A[1:]
        ]))
        print(f'{nodes=}')
        NodeGroup = {
            i: i
            for i in nodes
        }
        def getGroup(i: int) -> int:
            j = NodeGroup[i]
            if i != j:
                j = getGroup(j)
                NodeGroup[i] = j
            return j

        def sameGroup(i: int, j: int) -> bool:
            return getGroup(i) == getGroup(j)

        def mergeGroups(i: int, j: int):
            i = getGroup(i)
            j = getGroup(j)
            if i != j:
                NodeGroup[i] = j
            return
        
        for A in accounts:
            emails = A[1:]
            for E1, E2 in pairwise(emails):
                mergeGroups(E1, E2)
        
        # only after all the merges, we then do this:
        nameAndEmailsByGroup = {}
        for A in accounts:
            name = A[0]
            emails = A[1:]
            for E in emails:
                myGroup = getGroup(E)
                nameAndEmailsByGroup.setdefault(myGroup, {'name': name, 'emails': set()})
                assert nameAndEmailsByGroup[myGroup]['name'] == name
                nameAndEmailsByGroup[myGroup]['emails'].add(E)

        new_accounts = []
        for Group, Data in nameAndEmailsByGroup.items():
            print(f'Processing {Group=}')
            name = Data['name']
            emails = Data['emails']
            new_accounts.append(
                [name] + sorted(emails)
            )
        
        return new_accounts

# NOTE: Accepted on second Run (first was variable-name typo)
# NOTE: Accepted on first Submit
# NOTE: Runtime 208 ms Beats 18.09%
# NOTE: Memory 20.63 MB Beats 46.31%
