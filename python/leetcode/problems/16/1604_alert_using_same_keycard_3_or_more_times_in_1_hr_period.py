class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:

        def TimeStampToMinutes(timestamp: str) -> int:
            (H, M) = map(int, timestamp.split(':'))
            minutes = H * 60 + M
            # print(f'{timestamp=} {H=} {M=} {minutes=}')
            return minutes
        
        # testing = [
        #     TimeStampToMinutes(TS)
        #     for TS in ["13:00","13:20","14:00","18:00","18:51","19:30","19:49"]
        # ]
        
        data = {}
        for (name, timestamp) in zip(keyName, keyTime):
            data.setdefault(name, [])
            data[name].append(TimeStampToMinutes(timestamp))
        # print(f'{data=}')

        answers = []
        for name, timesArray in data.items():
            timesArray.sort()
            print(f'{name=} {timesArray=}')
            diffs = [
                B - A
                for A, B in zip(timesArray, timesArray[2:])
            ]
            print(f'{diffs=}')
            if diffs and min(diffs) <= 60:
                answers.append(name)
        answers.sort()
        return answers

