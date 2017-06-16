from os import environ
from redis import StrictRedis

def _redis_host():
    return environ.get('DATA_REDIS_HOST', '127.0.0.1')


def redis_connect():
    return StrictRedis(host=_redis_host(), port=6379, db=0)

class RedisDict(object):
    def __init__(self):
        self.redis = redis_connect()

    def __getitem__(self, k):
        return self.redis.get(k)

    def __setitem__(self, k, v):
        self.redis.set(k, v)