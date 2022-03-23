# pylint: disable=W0603
'''Redis memory cache library.'''
import redis

SCACHE = None

class MemoryCacheValueNotFound(Exception):
    '''Rised when value found.'''

class SCache():
    '''Access default memory cache.'''

    @staticmethod
    def init():
        '''Initialize memory cache.'''
        global SCACHE

        SCACHE = redis.StrictRedis('localhost', 6379, encoding="utf-8", decode_responses=True)

    @staticmethod
    def hset(hashkey, key, value):
        '''set a hash value.'''

        SCACHE.hset(hashkey, key, value)

    @staticmethod
    def hget(hashkey, key):
        '''get a specified value.'''

        ret_val = SCACHE.hget(hashkey, key)

        return ret_val

    @staticmethod
    def hdel(hashkey, key):
        '''delete a specified value.'''

        SCACHE.hdel(hashkey, key)

    @staticmethod
    def hexists(hashkey, key):
        '''check whether the specified value exist.'''
        return SCACHE.hexists(hashkey, key)

    @staticmethod
    def hkeys(hashkey):
        '''get all keys in the specified hash.'''
        return SCACHE.hkeys(hashkey)
