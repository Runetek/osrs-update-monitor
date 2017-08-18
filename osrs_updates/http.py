from flask import Flask, g, jsonify, send_from_directory
from werkzeug.local import LocalProxy
from datastore import PersistentDict
from os.path import join

app = Flask(__name__)


def get_redis():
    db = getattr(g, '_db', None)
    if db is None:
        db = g._db = PersistentDict()
    return db


db = LocalProxy(get_redis)

@app.route('/packs/<pack>.jar')
def gamepack(pack):
    if pack is not None:
        return send_from_directory('/app/static', '{}.jar'.format(pack), as_attachment=True)

@app.route('/')
def index():
    rev = db['revision']
    if rev is None:
        return jsonify(error='No data')
    elif type(rev) is str or type(rev) is unicode:
        rev = int(rev)
    return jsonify(release=rev)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
