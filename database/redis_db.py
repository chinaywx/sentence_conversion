import redis


class RedisDb:
    def __init__(self):
        pool = redis.ConnectionPool(host='192.168.2.106', port=6378, db=1, password='')
        self.r = redis.Redis(connection_pool=pool)
