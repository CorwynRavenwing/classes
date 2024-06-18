class Solution:
    def maskPII(self, s: str) -> str:

        if '@' in s:
            # email address
            s = s.lower()
            (name, domain) = s.split('@')
            print(f'Email: "{name}" @ "{domain}"')
            return name[0] + '*****' + name[-1] + '@' + domain
        else:
            for sepchar in '+-() ':
                s = s.replace(sepchar, '')
            phone = s[-10:]
            country = s[:-10]
            print(f'Phone: +"{country}" "{phone}"')
            country = '*' * len(country)
            phone = '***-***-' + phone[-4:]
            if len(country):
                return '+' + country + '-' + phone
            else:
                return phone

# NOTE: 33 ms; Beats 73.83%
