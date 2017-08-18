from json import dumps
import requests
from shutil import copyfileobj
from collections import OrderedDict

from world_list import WorldList


URL_WORLD_SL = 'http://www.runescape.com/g=oldscape/slr.ws?order=LPWM'

def download_worlds():
    r = requests.get(URL_WORLD_SL, stream=True)
    with open('/app/static/worlds.bin', 'wb') as f:
        copyfileobj(r.raw, f)
    del r


def world_to_dict(world):
    return OrderedDict([
        ('id', world.id),
        ('mask', world.mask),
        ('address', world.address),
        ('activity', world.activity),
        ('location', world.location),
        ('player_count', world.player_count)
    ])

def read_worlds(f):
    worlds = WorldList.from_file(f).worlds
    return sorted(map(world_to_dict, worlds), key=lambda x: x['id'])


def main():
    download_worlds()
    worlds = read_worlds('/app/static/worlds.bin')
    with open('/app/static/worlds.json', 'w') as f:
        f.write(dumps({'worlds': worlds}))


if __name__ == '__main__':
    main()
