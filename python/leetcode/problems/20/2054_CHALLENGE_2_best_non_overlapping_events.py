class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:

        debug = (len(events) < 500)
        if not debug:
            print(f'Note: {len(events)=} >= {500}, not printing details')

        scoresOfEventsEnding = {}
        eventsByStartTime = []
        for (start, end, score) in events:
            scoresOfEventsEnding.setdefault(end, [])
            scoresOfEventsEnding[end].append(score)
            bisect.insort(eventsByStartTime, (start, score))
        # print(f'{scoresOfEventsEnding=}')
        # print(f'{eventsByStartTime=}')

        REV = lambda x: list(reversed(list(x)))

        scoresByStartTime = [
            score
            for (startTime, score) in eventsByStartTime
        ]
        maxScoresFromRight = REV(itertools.accumulate(REV(scoresByStartTime), max))

        answers = []
        for (ending, scoreList) in scoresOfEventsEnding.items():
            if debug:
                print(f'FIRST {ending=} {scoreList=}')
            score1 = max(scoreList)
            target = (ending + 1, 0)
            index = bisect.bisect_left(eventsByStartTime, target)
            try:
                event = eventsByStartTime[index]
            except IndexError:
                event = None
            if debug:
                print(f'  SECOND {index=} {event=}')
            if event is None:
                score2 = None
                if debug:
                    print(f'    {score1=} {score2=}')
                answers.append(score1)  # first event by itself
                continue
            score2 = maxScoresFromRight[index]
            total = score1 + score2
            if debug:
                print(f'    {score1=} {score2=} {total=}')
            answers.append(total)

        if debug:
            print(f'{answers=}')
        return max(answers)

# NOTE: Runtime 363 ms Beats 27.67%
# NOTE: Memory 72.68 MB Beats 17.80%
