# Nathan Crapo's Midnight board. This file is for "hardware setup" -
# scanning, split operation etc.

import board
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.modules.split import Split, SplitSide
from storage import getmount

# fmt: off
# The right is a mirror image of the left side
_KEY_CFG_LEFT = [
    board.GP6,  board.GP9,  board.GP12, board.GP15, board.GP26, board.GP20,
    board.GP5,  board.GP8,  board.GP11, board.GP14, board.GP27, board.GP21,
    board.GP4,  board.GP7,  board.GP10, board.GP13, board.GP28, board.GP22,
                                        board.GP19, board.GP18, board.GP3,
]
# Fmt: on

# Do side auto-detect like 'Split' here so we can hard-code the target side,
# too. The target side can currently only be the right side.
drive_name = getmount('/').label
if drive_name.endswith('L'):
    split_side = SplitSide.LEFT
    print(f'Autodetected LEFT keyboard - Last letter of {drive_name} is L - USB: non-target')
else:
    split_side = SplitSide.RIGHT
    print('Autodetected RIGHT keyboard - target side')

# Note: Must change the volume name to end in an 'L' for left side and 'R' for
# right side auto-detection.
split = Split(
    uart_flip=False,
    data_pin=board.GP17,
    data_pin2=board.GP16,
    split_side=split_side,
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
