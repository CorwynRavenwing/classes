class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        data = Counter()
        for cpd in cpdomains:
            print(f'{cpd=}')
            (countStr, domain) = cpd.split()
            count = int(countStr)
            print(f'  {count=} {domain=}')
            subd = tuple(domain.split('.'))
            print(f'    {subd=}')
            while subd:
                print(f'      {subd} + {count}')
                data[subd] += count
                subd = subd[1:]
            print(f'    {subd=}')
        print(f'{data=}')

        answer = [
            f"{count} {'.'.join(domain)}"
            for domain, count in data.items()
        ]
        return answer
        
