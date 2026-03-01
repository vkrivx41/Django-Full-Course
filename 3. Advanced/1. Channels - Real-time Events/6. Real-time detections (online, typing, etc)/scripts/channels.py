from typing import List, Dict

from utilities.redis import presence

def run():

    redis_client = presence.RedisClient("127.0.0.1", 6379, 0)
    
    redis_client.connect("user1")
    redis_client.connect("user2")
    redis_client.connect("user3")
    redis_client.connect("user4")
    redis_client.connect("user5")

    redis_client.disconnect("user2")

    redis_client.heart_beat("user3")

    # redis_client.heart_beat("user1")
    # redis_client.heart_beat("user4")
    # redis_client.heart_beat("user5")

    print(redis_client.get_opponents_online_status(["user2", "user4", "userx"]))
