from contextlib import closing
from socket import create_connection
from struct import pack, unpack
from datastore import PersistentDict
from notifications import Notification, send_notification

HOST = 'oldschool1.runescape.com'
PORT = 43594

RESP_OUTDATED = 6

class UpdateChecker(object):
    def __init__(self, host=None, port=43594):
        self.host = host or HOST
        self.port = port

    def _is_outdated(self, reply):
        return RESP_OUTDATED == reply

    def _decode_reply(self, reply):
        return unpack('b', reply)[0]

    def _encode_request(self, revision):
        return pack('>bi', 15, revision)

    def _check_rev(self, revision):
        # Handshake code by pyroryan (pyro.ryan1988@gmail.com)
        # Original post: https://rs-hacking.com/forum/index.php?/topic/177-2/?p=1399

        with closing(create_connection((self.host, self.port))) as sock:
            sock.send(self._encode_request(revision))
            reply = self._decode_reply(sock.recv(1))
            return not self._is_outdated(reply)

    def run(self, start, limit=20):
        for rev in xrange(start, start + limit):
            if self._check_rev(rev):
                return rev
            else:
                print 'not {}'.format(rev)

def main():
    db = PersistentDict()
    checker = UpdateChecker(host='oldschool78.runescape.com')
    initial_revision = db['revision'] or 140
    if type(initial_revision) is str:
        initial_revision = int(initial_revision)
    current = checker.run(start=initial_revision)
    if current is not None:
        db['revision'] = current
        if current != initial_revision:
            n = Notification(title='OSRS Updated!', body='New revision={}, Old revision={}'.format(current, initial_revision))
            send_notification(n)


if __name__ == '__main__':
    main()
