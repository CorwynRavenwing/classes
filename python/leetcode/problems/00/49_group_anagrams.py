class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}
        for word in strs:
            key = tuple(sorted(word))
            groups.setdefault(key, [])
            groups[key].append(word)
        print(f'{groups=}')
        
        return [
            sorted(G)
            for key, G in groups.items()
        ]

# NOTE: Runtime 86 ms Beats 74.49%
# NOTE: Memory 21.44 MB Beats 31.33%
