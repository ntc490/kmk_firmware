# Nathan Crapo's Midnight board. This file is for "hardware setup" -
# scanning, split operation etc.

import board
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.modules.split import Split, SplitSide
from storage import getmount

# Must change this per side. Could we create a new file to contain it maybe?
leftSide = True

# fmt: off
# The right is a mirror image of the left side
_KEY_CFG_LEFT = [
    board.GP6,  board.GP9,  board.GP12, board.GP15, board.GP26, board.GP20,
    board.GP5,  board.GP8,  board.GP11, board.GP14, board.GP27, board.GP21,
    board.GP4,  board.GP7,  board.GP10, board.GP13, board.GP28, board.GP22,
                                        board.GP19, board.GP18, board.GP3,
]
# Fmt: on

# Note: might eventually change the Split obj - set uart_flip=False
# and define data_pin=GP17 (RX), data_pin2=GP16 (TX). But need to
# identify and provide side or let Split auto-detect side. Split
# determines side by looking at the last char of mount name 'L' is
# left, 'R' is right, BUT then 'target' is only defined by if USB is
# connected or not. Connecting USB to the wrong side would yield a
# non-working setup.

if (leftSide):
    split = Split(
        data_pin=board.GP16,
        split_side=SplitSide.LEFT,
        split_target_left=False,
    )
else:
    split = Split(
        data_pin=board.GP17,
        split_side=SplitSide.RIGHT,
        split_target_left=False,
    )

class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        # create and register the scanner
        self.matrix = KeysScanner(_KEY_CFG_LEFT)
        self.modules = [ split ]


    # flake8: noqa
    # fmt: off
    coord_mapping = [
        0,  1,  2,  3,  4,  5,     26, 25, 24, 23, 22, 21,
        6,  7,  8,  9,  10, 11,    32, 31, 30, 29, 28, 27,
        12, 13, 14, 15, 16, 17,    38, 37, 36, 35, 34, 33,
                    18, 19, 20,    41, 40, 39,
    ]
