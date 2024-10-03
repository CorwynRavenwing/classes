class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:

        servers = len(patience)

        # SHORTCUT: Each server may send a lot of messages to
        # the master server, but we only care about two of them:
        # (1) the *first* message each server sends, when the
        #   master server receives it, and when the server
        #   receives its reply and STOPS sending retries.
        # (2) the *last* message each server sends, which happens
        #   at the final resend opportunity *strictly before*
        #   the time of receiving return message (1)

        # 0: we turn 'edges' array into 'adjacent' links:

        adjacent = {}
        for i in range(servers):
            adjacent.setdefault(i, set())
        for (Ui, Vi) in edges:
            adjacent[Ui].add(Vi)
            adjacent[Vi].add(Ui)
        # print(f'{adjacent=}')
        
        # 1: we determine the time distance from the master server
        #   to each other server, which equals the reverse path time:

        Master = 0
        distanceToServer = {Master: 0}
        distance = 0
        # print(f'{distance=}')
        # print(f'  Master')
        # print(f'    N={Master}')
        queue = {Master}
        while queue:
            distance += 1
            # print(f'{distance=}')
            newQ = set()
            for S in queue:
                # print(f'  {S=}')
                for N in adjacent[S]:
                    # print(f'    {N=}')
                    if N in distanceToServer:
                        # print(f'      seen ({distanceToServer[N]})')
                        continue
                    else:
                        distanceToServer[N] = distance
                        newQ.add(N)
            queue = newQ
        # print(f'{distanceToServer=}')

        oneWayTimes = [
            distanceToServer[i]
            for i in range(servers)
        ]
        # print(f'{oneWayTimes=}')
        roundTripTimes = [
            2 * time
            for time in oneWayTimes
        ]
        # print(f'{roundTripTimes=}')

        # 2: when does the reply arrive for the first message sent?

        firstReplyArrives = roundTripTimes
        # print(f'{firstReplyArrives=}')

        # 3: when does each data server send its last message?

        PriorModValue = lambda value, mod: ((value // mod) * mod) if mod else 0
        # === X where (X < value) and (X % mod == 0)
        # null case 0 -> 0

        lastMessageSent = [
            PriorModValue(FR - 1, P)
            for (FR, P) in zip(firstReplyArrives, patience)
        ]
        # print(f'{lastMessageSent=}')

        # 4: when does the last message arrive at the master server?

        lastMessageReceived = [
            sentTime + roundTrip
            # a round-trip time starting when we sent it
            for (sentTime, roundTrip) in zip(lastMessageSent, roundTripTimes)
        ]
        # print(f'{lastMessageReceived=}')

        # we don't actually need to combine this data with "firstReplyArrives",
        # because if "sentTime" == 0 (i.e. no re-sends were sent),
        # then 1RA == LMR, and if "sentTime" > 0, then 1RA < LMR, therefore
        # max(LMR) will always === max(LMR, 1RA)

        lastNonIdleSecond = max(lastMessageReceived)
        firstIdleSecond = lastNonIdleSecond + 1

        return firstIdleSecond

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (first was Output Exceeded)
# NOTE: Runtime 1914 ms Beats 16.31%
# NOTE: Memory 88.67 MB Beats 6.15%
