# Nathan Crapo's Midnight board. This file is for "hardware setup" -
# scanning, split operation etc.

import board
from kmk.keys import KC
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

class Mapper42():
    # Create 42 kep Midnight keyboard map by separately defining the
    # left and right sides. Just makes definition easier to read.
    def __init__(self):
        self._map = [0] * 42

    def left(self, *keys):
        self._map[0] = keys[0]
        self._map[1] = keys[1]
        self._map[2] = keys[2]
        self._map[3] = keys[3]
        self._map[4] = keys[4]
        self._map[5] = keys[5]
        self._map[12] = keys[6]
        self._map[13] = keys[7]
        self._map[14] = keys[8]
        self._map[15] = keys[9]
        self._map[16] = keys[10]
        self._map[17] = keys[11]
        self._map[24] = keys[12]
        self._map[25] = keys[13]
        self._map[26] = keys[14]
        self._map[27] = keys[15]
        self._map[28] = keys[16]
        self._map[29] = keys[17]
        self._map[36] = keys[18]
        self._map[37] = keys[19]
        self._map[38] = keys[20]

    def right(self, *keys):
        self._map[6] = keys[0]
        self._map[7] = keys[1]
        self._map[8] = keys[2]
        self._map[9] = keys[3]
        self._map[10] = keys[4]
        self._map[11] = keys[5]
        self._map[18] = keys[6]
        self._map[19] = keys[7]
        self._map[20] = keys[8]
        self._map[21] = keys[9]
        self._map[22] = keys[10]
        self._map[23] = keys[11]
        self._map[30] = keys[12]
        self._map[31] = keys[13]
        self._map[32] = keys[14]
        self._map[33] = keys[15]
        self._map[34] = keys[16]
        self._map[35] = keys[17]
        self._map[39] = keys[18]
        self._map[40] = keys[19]
        self._map[41] = keys[20]

    def map(self):
        return self._map

class Mapper36():
    layer_count = 0

    # Create 36 kep Midnight keyboard map by separately defining the
    # left and right sides. Just makes definition easier to read.
    def __init__(self):
        self._map = [0] * 42
        self._layer_id = Mapper36.layer_count
        Mapper36.layer_count += 1

    def left(self, *keys):
        self._map[0] = KC.NO
        self._map[1] = keys[0]
        self._map[2] = keys[1]
        self._map[3] = keys[2]
        self._map[4] = keys[3]
        self._map[5] = keys[4]
        self._map[12] = KC.NO
        self._map[13] = keys[5]
        self._map[14] = keys[6]
        self._map[15] = keys[7]
        self._map[16] = keys[8]
        self._map[17] = keys[9]
        self._map[24] = KC.NO
        self._map[25] = keys[10]
        self._map[26] = keys[11]
        self._map[27] = keys[12]
        self._map[28] = keys[13]
        self._map[29] = keys[14]
        self._map[36] = keys[15]
        self._map[37] = keys[16]
        self._map[38] = keys[17]

    def right(self, *keys):
        self._map[6]  = keys[0]
        self._map[7]  = keys[1]
        self._map[8]  = keys[2]
        self._map[9]  = keys[3]
        self._map[10] = keys[4]
        self._map[11] = KC.NO
        self._map[18] = keys[5]
        self._map[19] = keys[6]
        self._map[20] = keys[7]
        self._map[21] = keys[8]
        self._map[22] = keys[9]
        self._map[23] = KC.NO
        self._map[30] = keys[10]
        self._map[31] = keys[11]
        self._map[32] = keys[12]
        self._map[33] = keys[13]
        self._map[34] = keys[14]
        self._map[35] = KC.NO
        self._map[39] = keys[15]
        self._map[40] = keys[16]
        self._map[41] = keys[17]

    @property
    def layer_id(self):
        return self._layer_id

    def map(self):
        return self._map

def add_keyboard_layer(keyboard, *layers):
    # Ensure keyboard layers are added in proper order
    for id in range(len(layers)):
        for layer in layers:
            if layer.layer_id == id:
                keyboard.keymap.append(layer.map())
                break
