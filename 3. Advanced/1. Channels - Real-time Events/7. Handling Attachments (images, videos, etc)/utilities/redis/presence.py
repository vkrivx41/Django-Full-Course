from typing import List, Dict

import redis


class RedisClient:
    CONNETIONS_KEY = "connections:user_{user_id}"
    ONLINE_KEY = "online:user_{user_id}"

    TTL = 20  # 20 seconds to expire

    def __init__(self, host_name: str, port: int, db_number: int):
        self.redis_client = redis.Redis(
            host=host_name,
            port=port,
            db=db_number,
            decode_responses=True,
            socket_timeout=2,
            socket_connect_timeout=2
        )

    def format_keys(self, user_id) -> tuple:
        return (
            self.CONNETIONS_KEY.format(user_id=user_id),
            self.ONLINE_KEY.format(user_id=user_id)
        )

    def connect(self, user_id):
        """
        -> format the connections and online keys
        -> increase the number of connections by 1
        -> if the number of connections is 1 (first time) or the online key doesn't exist
            then add online key and set the connections key to 1 (restart if not 1) and return True
        -> return False otherwise
        """
        connections_key, online_key = self.format_keys(user_id)

        connections_count: int = int(self.redis_client.incr(connections_key))
        online_key_exists: bool = self.redis_client.get(online_key)

        if connections_count == 1 or not online_key_exists:
            self.redis_client.set(connections_key, 1)
            self.redis_client.set(online_key, 1, ex=self.TTL)
            return True
        
        return False

    def disconnect(self, user_id):
        """
        -> format the connections and online keys
        -> decrease the number of connections by 1
        -> if the number of connections is 0 (last time) or the online key doesn't exist
            then remove the connections and online keys and return True
        -> return False otherwise
        """
        connections_key, online_key = self.format_keys(user_id)

        connections_count: int = int(self.redis_client.decr(connections_key))
        online_key_exists: bool = self.redis_client.get(online_key)

        if connections_count == 0 or not online_key_exists:
            self.redis_client.delete(connections_key)
            self.redis_client.delete(online_key)
            return True
        
        return False
    
    def heartbeat(self, user_id) -> bool:
        """
        -> format the connections key
        -> re-update the TTL to the pre-defined TTL (normally 60s) if the online key exists
            otherwise delete the connections key and return false
        """
        connections_key, online_key = self.format_keys(user_id)

        if self.redis_client.get(online_key):
            self.redis_client.expire(online_key, self.TTL)
            return True
        
        self.redis_client.delete(connections_key)
        
        return False


    def get_opponents_online_status(self, opponent_ids: List[str]) -> Dict[str, bool]:
        """
        return something like
        {
            "user1": True,
            "user2" : False
        }
        """

        if not opponent_ids:
            return {}
        
        # create a pipeline that can run multiple commands at once in bulk mode
        pipe = self.redis_client.pipeline()

        for uid in opponent_ids:
            online_key = self.ONLINE_KEY.format(user_id=uid)
            pipe.exists(online_key, uid)

        online_result = pipe.execute()
        
        # map to get the final dict obj
        return {
            uid: bool(status)
            for uid, status in zip(opponent_ids, online_result)
        }
    