class Twitter:

    def __init__(self):
        self.tweets=[]
        self.following={}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.follow(userId,userId)
        self.tweets.append([userId,tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        rt=[]
        try:
            for k in self.tweets[::-1]:
                for i in self.following[userId]:
                    if k[0] == i and k[1] not in rt:
                        rt.append(k[1])
            if len(rt) >= 10:
                return rt[:10]
        except:
            pass
        finally:
            return rt[:10]


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].append(followeeId)
        else:
            self.following[followerId]=[followeeId]
    def unfollow(self, followerId: int, followeeId: int) -> None:
        try:
            self.following[followerId].remove(followeeId)
        except ValueError:
            pass
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)