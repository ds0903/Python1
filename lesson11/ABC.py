from abc import ABC, abstractmethod
from datetime import datetime
import time
from dataclasses import dataclass

start_time = time.time()

@dataclass
class Post:
    message: str
    timestamp: datetime  

class SocialChannel(ABC): 
    def __init__(self, channel: str, followers: int) -> None:
        self.channel = channel
        self.followers = followers
        
    @abstractmethod
    def post_m(self, message: str) -> None:
        pass

class YouTubeChannel(SocialChannel):
    def post_m(self, message) -> None:
        print(f"Опубліковано на Ютуб: {message}")

class FacebookChannel(SocialChannel):
    def post_m(self, message) -> None:
        print(f"Опубліковано на Фейсбук: {message}")

class TwitterChannel(SocialChannel):
    def post_m(self, message) -> None:
        print(f"Опубліковано на Твітер: {message}")

class TelegamChannel(SocialChannel):
    def post_m(self, message) -> None:
        print(f"Опубліковано на Телеграм: {message}")

def post_a_message(channel: SocialChannel, message) -> None:
    channel.post_m(message)

def process_schedule(posts: list[Post], channels: list[SocialChannel]) -> None:
    #current_time = datetime.now()
    for post in posts:
        message, timestamp = post.message, post.timestamp
        if timestamp <= datetime.now():
            for channel in channels:
                channel.post_m(message)

# Список каналів
channels_list = [
    YouTubeChannel("youtube", 1000),
    FacebookChannel("facebook", 500),
    TwitterChannel("twitter", 200),
    TelegamChannel("telegram", 3500)
]

# Пости
post_now1 = Post("Hello YouTube!", datetime.now())
post_now2 = Post("Привіт фейсбук", datetime.now())
post_now3 = Post("Hi Твіттер!", datetime.now())
post_now4 = Post("Привет Телеграм!", datetime.now())


process_schedule(
    posts=[post_now1, post_now2, post_now3, post_now4],
    channels=channels_list
)

end_time = time.time()
execution_time = end_time - start_time
print(f"Програма зайняла {execution_time} секунд твого часу")    