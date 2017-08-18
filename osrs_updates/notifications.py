from collections import namedtuple
from os import environ
from pushover import Client

Notification = namedtuple('Notification', ['body', 'title'])

USER_KEY = environ.get('PUSHOVER_USER_KEY')
API_TOKEN = environ.get('PUSHOVER_API_TOKEN', False)


def send_notification(notification):
    if not API_TOKEN:
        print 'No Pushover API token set'
        return

    client = Client(USER_KEY, api_token=API_TOKEN)
    client.send_message(notification.body, title=notification.title)
