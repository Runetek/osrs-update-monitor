from collections import namedtuple
from os import environ
from pushover import Client

Notification = namedtuple('Notification', ['body', 'title'])

USER_KEY = environ.get('PUSHOVER_USER_KEY')
API_TOKEN = environ.get('PUSHOVER_API_TOKEN')


def send_notification(notification):
    client = Client(USER_KEY, api_token=API_TOKEN)
    client.send_message(notification.body, title=notification.title)
