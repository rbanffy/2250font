#!/usr/bin/env python3

import argparse
import sys

parser = argparse.ArgumentParser(description='Generate a grid for 2250font.')

# Character is within a rectangle (0, -200) to (516, 800)
XMIN = 0
YMIN = -200
XMAX = 516
YMAX = 800

GUIDE_XMIN = XMIN - 200
GUIDE_XMAX = XMAX + 200

GUIDE_YMIN = YMIN - 200
GUIDE_YMAX = YMAX + 200

parser.add_argument('min_x', type=float, default=XMIN, help='Minimum X')
parser.add_argument('min_y', type=float, default=YMIN, help='Minimum Y')
parser.add_argument('max_x', type=float, default=XMAX, help='Maximum X')
parser.add_argument('max_y', type=float, default=YMAX, help='Maximum Y')
parser.add_argument(
    'divs_x',
    type=float,
    default=7,
    help='Horizontal divisions from origin to max X',
)
parser.add_argument(
    'divs_y',
    type=float,
    default=7,
    help='Vertical divisions from origin to max Y',
)

args = parser.parse_args()

delta_x = args.max_x / args.divs_x
delta_y = args.max_y / args.divs_y

if __name__ == '__main__':
    print('#', ' '.join(sys.argv))

    print('Grid')

    # Guides extend 200 units away from the character box
    guide_xmin = args.min_x - 200
    guide_xmax = args.max_x + 200
    guide_ymin = args.min_y - 200
    guide_ymax = args.max_y + 200

    # Each guide line is described by a point (x y m 0) and a line
    # (x y l 1024). It can optionally be named.

    # Draw the origin lines.
    print(
        '{:.0f} {:.0f} m 0 {:.0f} {:.0f} l 1024 Named: "Origin X"'.format(
            0, guide_ymin, 0, guide_ymax
        )
    )
    print(
        '{:.0f} {:.0f} m 0 {:.0f} {:.0f} l 1024 Named: "Origin Y"'.format(
            guide_xmin, 0, guide_xmax, 0
        )
    )

    # Draw horizontals above the origin.
    y = delta_y
    while y < args.max_y + delta_y:
        print(
            '{:.0f} {:.0f} m 0 {:.0f} {:.0f} l 1024 Named: "{:.0f}"'.format(
                guide_xmin, y, guide_xmax, y, y
            )
        )
        y += delta_y

    # Draw horizontals below the origin.
    y = -delta_y
    while y > args.min_y:
        print(
            '{:.0f} {:.0f} m 0 {:.0f} {:.0f} l 1024 Named: "{:.0f}"'.format(
                guide_xmin, round(y, 0), guide_xmax, round(y, 0), y
            )
        )
        y -= delta_y

    # Draw verticals to the right of the origin.
    x = delta_x
    while x < args.max_x:
        print(
            '{:.0f} {:.0f} m 0 {:.0f} {:.0f} l 1024 Named: "{:.0f}"'.format(
                round(x, 0), guide_ymin, round(x, 0), guide_ymax, x
            )
        )
        x += delta_x

    # And to the left.
    x = 0 - delta_x
    while x > args.min_x:
        print(
            '{:.0f} {:.0f} m 0 {:.0f} {:.0f} l 1024 Named: "{:.0f}"'.format(
                round(x, 0), guide_xmin, round(x, 0), guide_xmax, x
            )
        )
        x -= delta_x

    print('EndSplineSet')
