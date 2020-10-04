import abc

class IStorage(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def save_tweet(self, tweet: object) -> bool:
        pass

    @abc.abstractmethod
    def save_user_tweets(self, user_tweets: object) -> bool:
        pass

