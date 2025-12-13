class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        
        events_by_timestamp = [
            (
                int(timestamp),
                (1 if messagetype == "OFFLINE" else 2),
                messagetype,
                argument,
            )
            for (messagetype, timestamp, argument) in events
        ]
        events_by_timestamp.sort()
        print(f'{events_by_timestamp=}')

        offline = set()
        answer = [0] * numberOfUsers
        all_calls = 0

        while events_by_timestamp:
            (timestamp, order, messagetype, argument) = events_by_timestamp.pop(0)
            print(f'{timestamp=}')
            if messagetype == 'OFFLINE':
                id = int(argument)
                offline.add(id)
                then = timestamp + 60
                print(f'  {id} going offline till {then}')
                print(f'    ({offline=})')
                event = (then, 0, 'ONLINE', argument)
                # print(f'\nDEBUG: INSORT ERROR\n{event=}\n{events_by_timestamp=}')
                bisect.insort(events_by_timestamp, event)
            elif messagetype == 'ONLINE':
                id = int(argument)
                if id in offline:
                    print(f'  {id} coming back online')
                    offline.remove(id)
                    print(f'    ({offline=})')
                else:
                    print(f'    {id} IS ALREADY ONLINE')
            elif messagetype == 'MESSAGE':
                if argument == 'ALL':
                    all_calls += 1
                    print(f'  ALL:{all_calls}')
                elif argument == 'HERE':
                    all_calls += 1
                    print(f'  HERE:')
                    print(f'    +ALL:{all_calls}')
                    for id in offline:
                        print(f'    -{id}')
                        answer[id] -= 1
                else:
                    ids = argument.split(' ')
                    print(f'  LIST:')
                    for id_str in ids:
                        id_str = id_str.replace('id', '')
                        id = int(id_str)
                        print(f'    +{id}')
                        answer[id] += 1
        
        answer = [
            A + all_calls
            for A in answer
        ]

        return answer

# NOTE: Acceptance Rate 35.9% (medium)

# NOTE: Accepted on third Run (typos)
# NOTE: Accepted on second Submit (order-of-operations guess was incorrect)
# NOTE: Runtime 119 ms Beats 9.51%
# NOTE: Memory 18.35 MB Beats 7.22%
