from typing import List
import heapq

class Twitter:

    def __init__(self):
        self.follower = {}
        self.tweet = {}
        self.time = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweet:
            self.tweet[userId].append((self.time, tweetId))

        else:
            self.tweet[userId] = [(self.time, tweetId)]

        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        feed = []

        feed.extend(self.tweet.get(userId, []))
        for user in self.follower.get(userId, []):
            feed.extend(self.tweet.get(user, []))

        heapq.heapify(feed)
        for _ in range(min(len(feed), 10)):
            _, tweet = heapq.heappop(feed)
            res.append(tweet)

        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follower:
            self.follower[followerId].add(followeeId)

        else:
            self.follower[followerId] = {followeeId}


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follower:
            self.follower[followerId].remove(followeeId)

"""
Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(userId,tweetId)
param_2 = obj.getNewsFeed(userId)
obj.follow(followerId,followeeId)
obj.unfollow(followerId,followeeId)
"""

#---------------------------------------------------------
#           Time Complexity:
#           postTweet:       O(1)
#           getNewsFeed:     O(n)
#           follow:          O(1)
#           unfollow:        O(1)
#           
#           Space Complexity:
#           O(n)
#---------------------------------------------------------