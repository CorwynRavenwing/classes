class Solution:
    def validIPAddress(self, queryIP: str) -> str:

        def containsInvalidChars(string: str, allowed: str) -> bool:
            for ch in string:
                if ch not in allowed:
                    # print(f'DEBUG: "{ch}" not in "{allowed}"')
                    return True
            return False
        
        def isValidIPv4(queryIP: str) -> bool:
            allowed = '0123456789'

            if '.' not in queryIP:
                return False
            
            octets = queryIP.split('.')
            print(f'{octets=}')

            if len(octets) != 4:
                print(f'not 4 octets')
                return False
            
            for octet in octets:
                if containsInvalidChars(octet, allowed):
                    print(f'{octet}: invalid characters')
                    return False
                
                if not (1 <= len(octet) <= 3):
                    print(f'{octet}: outside 1-3 length range')
                    return False

                if not (0 <= int(octet) <= 255):
                    print(f'{octet}: outside 0-255 range')
                    return False
                
                if octet != '0' and octet[0] == '0':
                    print(f'{octet}: leading zero')
                    return False

            return True

        def isValidIPv6(queryIP: str) -> bool:
            allowed = '0123456789abcdefABCDEF'
            
            if ':' not in queryIP:
                return False
            
            octets = queryIP.split(':')
            print(f'{octets=}')
            if len(octets) != 8:
                print(f'not 8 octets')
                return False

            for octet in octets:
                if containsInvalidChars(octet, allowed):
                    print(f'{octet}: invalid characters')
                    return False

                if not (1 <= len(octet) <= 4):
                    print(f'{octet}: outside 1-4 length range')
                    return False
                    
            return True
            
        if isValidIPv4(queryIP):
            return 'IPv4'

        if isValidIPv6(queryIP):
            return 'IPv6'

        return 'Neither'

# NOTE: 31 ms; Beats 79.55% of users with Python3
