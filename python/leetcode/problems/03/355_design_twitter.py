class Twitter:

    def __init__(self):
        self.tweets = {}
        self.follows = {}
        self.tweetOrder = []
        print("INIT")

    def createUser(self, userId: int) -> None:
        self.tweets.setdefault(userId, [])
        self.follows.setdefault(userId, [])
        return

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.createUser(userId)
        self.tweets[userId].append(tweetId)
        self.tweetOrder.append(tweetId)
        print(f'twit[{userId}]={self.tweets}')

    def getNewsFeed(self, userId: int) -> List[int]:

        def byTweetOrder(tweetId: int):
            return -self.tweetOrder.index(tweetId)
        
        self.createUser(userId)
        users = [userId] + self.follows[userId]
        print(f'showing {users=}')
        twits = [
            twit
            for user in users
            for twit in self.tweets[user]
        ]
        twits.sort(
            key=byTweetOrder
        )
        return twits[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.createUser(followerId)
        self.createUser(followeeId)
        if followeeId not in self.follows[followerId]:
            self.follows[followerId].append(followeeId)
        print(f'foll[{followerId}]={self.follows}')

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.createUser(followerId)
        self.createUser(followeeId)
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        print(f'unfoll[{followerId}]={self.follows}')

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

# NOTE: 20 ms; Beats 99.54% of users with Python3
# NOTE: 16.59 MB; Beats 97.22% of users with Python3
