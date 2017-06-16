from flask import Flask, g, jsonify
from cache import redis_connect
from werkzeug.local import LocalProxy
from datastore import RedisDict

app = Flask(__name__)


def get_redis():
    db = getattr(g, '_db', None)
    if db is None:
        db = g._db = RedisDict()
    return db


db = LocalProxy(get_redis)

@app.route('/')
def index():
    rev = db['revision']
    if rev is None:
        return jsonify(error='No data')
    elif type(rev) is str or type(rev) is unicode:
        rev = int(rev)
    return jsonify(release=rev)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
