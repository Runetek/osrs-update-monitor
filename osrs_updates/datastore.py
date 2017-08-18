from os import environ
from json import dumps, loads


# def _redis_host():
#     return environ.get('DATA_REDIS_HOST', '127.0.0.1')


# def _redis_connect():
#     return StrictRedis(host=_redis_host(), port=6379, db=0)


def PersistentDict():
    return JsonDict('/app/static/revision.json')


class JsonDict(object):
    def __init__(self, file):
        self._file = file
        self._data = {}

    def _open_file(self, mode='r'):
        return open(self._file, mode)

    def _read(self):
        with self._open_file() as f:
            self._data = loads(f.read())
            return self._data

    def _write(self):
        with self._open_file('w') as f:
            f.write(dumps(self._data))

    def __getitem__(self, k):
        return self._read().get(k)

    def __setitem__(self, k, v):
        self._data[k] = v
        self._write()


class RedisDict(object):
    def __init__(self):
        self._cache = _redis_connect()

    def __getitem__(self, k):
        return self._cache.get(k)

    def __setitem__(self, k, v):
        self._cache.set(k, v)
