#!/usr/bin/env python

from itertools import product
from random import shuffle, choice
from time import strftime
import argparse

from PIL import Image

from map_colors import TERRAIN_COLOR, ENEMY_COLOR, ALLIANCE_COLOR, WALL_COLOR


parser = argparse.ArgumentParser(description='Generates map for U5 exercise.')

parser.add_argument('-x', '--width', dest='width', type=int, default=800,
                    help='map width (default: 800)')

parser.add_argument('-y', '--height', dest='height', type=int, default=600,
                    help='map height (default: 600)')

parser.add_argument('-e', '--enemies', dest='enemies', type=float, default=0.5,
                    help='enemies number rate (0.0 - 1.0; default: 0.5)')

parser.add_argument('-a', '--alliance', dest='alliance', type=float, default=0.5,
                    help='aliance number rate (0.0 - 1.0; default: 0.5)')

parser.add_argument('-w', '--wall', dest='wall', type=float, default=0.5,
                    help='wall number rate (0.0 - 1.0; default: 0.5)')

if __name__ == '__main__':
    args = parser.parse_args()
    pixels = list(product(xrange(args.width), xrange(args.height)))
    shuffle(pixels)

    board = Image.new('RGB', (args.width, args.height), TERRAIN_COLOR)
    canvas = board.load()

    wall_length = int(args.width * args.height * 0.03 * args.wall)
    wall_position = None
    directions = {
        'down': (0, 1),
        'right': (1, 0),
    }
    wall_dir = 'down'
    wall_pixels = set()
    while wall_length:
        if wall_position is None:
            wall_position = pixels.pop()
        canvas[wall_position] = WALL_COLOR
        wall_length -= 1
        wall_pixels.add(wall_position)

        wall_dir = choice(directions.keys() * 3 + [wall_dir] * 6 + [None])
        if wall_dir is None:
            wall_position = None
            wall_dir = 'down'
            continue

        wall_position = (wall_position[0] + directions[wall_dir][0], wall_position[1] + directions[wall_dir][1])

        if not (args.width > wall_position[0] >= 0 and 0 <= wall_position[1] < args.height):
            wall_position = None

    pixels = list(set(pixels).difference(wall_pixels))
    shuffle(pixels)

    for unit in ((args.enemies, ENEMY_COLOR), (args.alliance, ALLIANCE_COLOR)):
        for i in xrange(int(args.width * args.height * 0.01 * unit[0])):
            canvas[pixels.pop()] = unit[1]

    filename = 'u5-board-%s.png' % strftime('%Y%m%d%H%M%S')
    board.save(filename, 'PNG')
    print filename

