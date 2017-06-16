from contextlib import closing
from socket import create_connection
from struct import pack, unpack
from datastore import DB

HOST = 'oldschool1.runescape.com'
PORT = 43594

RESP_OUTDATED = 6

def encode_handshake(revision):
    return pack('>bi', 15, revision)

def decode_handshake(sock):
    return unpack('b', sock.recv(1))[0]

class UpdateChecker(object):
    def __init__(self, host=None, port=43594):
        self.host = host or HOST
        self.port = port

    def _is_outdated(self, reply):
        return RESP_OUTDATED == reply

    def _decode_reply(self, reply):
        return unpack('b', reply)[0]

    def _check_rev(self, revision):
        # Handshake code by pyroryan (pyro.ryan1988@gmail.com)
        # Original post: https://rs-hacking.com/forum/index.php?/topic/177-2/?p=1399

        with closing(create_connection((self.host, self.port))) as sock:
            sock.send(encode_handshake(revision))
            reply = self._decode_reply(sock.recv(1))
            return not self._is_outdated(reply)

    def run(self, start, limit=20):
        for rev in xrange(start, start + limit):
            if self._check_rev(rev):
                return rev
            else:
                print 'not {}'.format(rev)

def main():
    db = DB()
    checker = UpdateChecker(host='oldschool78.runescape.com')
    initial_revision = db['revision'] or 140
    if type(initial_revision) is str:
        initial_revision = int(initial_revision)
    current = checker.run(start=initial_revision)
    if current is not None:
        db['revision'] = current


if __name__ == '__main__':
    main()
