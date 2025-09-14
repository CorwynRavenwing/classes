class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:

        # this set of functions is TRANSITIONS from one class to another

        @cache
        def learnedOnDay(D: int) -> int:
            print(f'learned({D})')
            if D <= 0:
                return 0    # base case prior to secret existing
            elif D == 1:
                return 1    # first person learns secret
            else:
                return canTellOnDay(D)  # each person who can tell, does
        
        @cache
        def becameAbleToTellOnDay(D: int) -> int:
            print(f'newTell({D})')
            if D <= 0:
                return 0    # base case prior to secret existing
            # elif forget <= delay:
            #     # actually, this is forbidden by constraint "1 <= delay < forget <= n"
            #     return 0    # everyone forgets before they can tell
            else:
                return learnedOnDay(D - delay)    # 'tell' delay has expired
        
        @cache
        def forgotOnDay(D: int) -> int:
            print(f'forgot({D})')
            if D <= 0:
                return 0    # base case prior to secret existing
            else:
                return learnedOnDay(D - forget)   # 'forget' delay has expired
        
        # this set of functions is MEMBER COUNTS of various classes

        @cache
        def knowsButCannotTellOnDay(D: int) -> int:
            print(f'+Know -Tell({D})')
            if D <= 0:
                return 0    # base case prior to secret existing
            else:
                return sum([
                    knowsButCannotTellOnDay(D - 1),    # yesterday's set
                    learnedOnDay(D),                # new today
                    -becameAbleToTellOnDay(D),      # moved into next group today
                ])
        
        @cache
        def canTellOnDay(D: int) -> int:
            print(f'+Know +Tell({D})')
            if D <= 0:
                return 0    # base case prior to secret existing
            else:
                return sum([
                    canTellOnDay(D - 1),        # yesterday's set
                    becameAbleToTellOnDay(D),   # moved from prior group today
                    -forgotOnDay(D),            # forgot the secret
                ])
        
        # no cache here, this fn is only ever called once
        # @cache
        def hasSecretOnDay(D: int) -> int:
            print(f'+Know({D})')
            if D <= 0:
                return 0    # base case prior to secret existing
            else:
                return sum([
                    knowsButCannotTellOnDay(D), # knows secret: cannot tell
                    canTellOnDay(D),            # knows secret: can tell
                ])

        mod = 10 ** 9 + 7

        return hasSecretOnDay(n) % mod

# NOTE: Acceptance Rate 47.4% (medium)

# NOTE: re-ran for challenge:
# NOTE: Runtime 123 ms Beats 32.12%
# NOTE: Memory 21.84 MB Beats 5.11%
