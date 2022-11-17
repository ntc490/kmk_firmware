# Nathan Crapo's Midnight board

import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard

from kmk.scanners.keypad import KeysScanner

from storage import getmount

#ALT board.GP16,
#ENTER board.GP18,
#CTRL board.GP19,
#Y board.GP20,
#H board.GP21,
#N board.GP22,
#U board.GP26,
#J board.GP27,
#M board.GP28,
# SHFT    board.GP4,
# "    board.GP5,
# \    board.GP6,
# /    board.GP7,
# ;    board.GP8,
# P    board.GP9,
# >    board.GP10,
# L    board.GP11,
# O    board.GP12,
# <    board.GP13,
# K    board.GP14,
# I    board.GP15,


# fmt: off
_KEY_CFG_RIGHT = [
    board.GP20, board.GP26, board.GP15, board.GP12, board.GP9,  board.GP6,
    board.GP21, board.GP27, board.GP14, board.GP11, board.GP8,  board.GP5,
    board.GP22, board.GP28, board.GP13, board.GP10, board.GP7,  board.GP4,
                                        board.GP16, board.GP18, board.GP19
]
# Fmt: on

class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        # create and register the scanner
        self.matrix = KeysScanner(_KEY_CFG_RIGHT)

    # flake8: noqa
    # fmt: off
    coord_mapping = [
        0,  1,  2,  3,  4,  5,
        6,  7,  8,  9,  10, 11,
        12, 13, 14, 15, 16, 17,
                    18, 19, 20,
    ]
