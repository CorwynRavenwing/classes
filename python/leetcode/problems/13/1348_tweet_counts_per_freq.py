class TweetCounts:

    def __init__(self):
        self.tweetCounts = {}
        return
    
    def createName(self, tweetName: str) -> None:
        self.tweetCounts.setdefault(tweetName, [])
        return

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.createName(tweetName)
        bisect.insort(self.tweetCounts[tweetName], time)
        return

    def getTweetCountsPerChunk(self, tweetName: str, startTime: int, endTime: int, chunkSize: int) -> List[int]:
        self.createName(tweetName)
        # print(f'gTCPC({tweetName},{startTime}-{endTime},{chunkSize})')
        TN = self.tweetCounts[tweetName]
        # print(f'Tweets: {TN}')
        beginChunk = startTime
        beginIndex = bisect_left(TN, beginChunk)
        answers = []
        while beginChunk <= endTime:
            endChunk = min(endTime, beginChunk + chunkSize - 1)
            endIndex = bisect_right(TN, endChunk)
            # print(f'Chunk {beginChunk}-{endChunk}:')
            indexes = endIndex - beginIndex
            # print(f'  indexes [{beginIndex}:{endIndex}]: {indexes}')
            answers.append(indexes)
            beginChunk = endChunk + 1
            beginIndex = endIndex
        return answers

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        chunkSize = None
        match freq:
            case "minute":
                chunkSize = 60
            case "hour":
                chunkSize = 3600
            case "day":
                chunkSize = 86400
            case _:
                raise ValueError(f'bad freq data "{freq}"')
        return self.getTweetCountsPerChunk(tweetName, startTime, endTime, chunkSize)

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)

# NOTE: 207 ms; Beats 88.33%
# O(log N)
