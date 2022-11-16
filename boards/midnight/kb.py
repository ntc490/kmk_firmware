# Nathan Crapo's Midnight board

import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard

from kmk.scanners.keypad import KeysScanner

from storage import getmount

# fmt: off
_KEY_CFG_RIGHT = [
     board.GP17, board.GP16
]
# fmt: on

class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        # create and register the scanner
        self.matrix = KeysScanner(_KEY_CFG_RIGHT)

    # flake8: noqa
    # fmt: off
    coord_mapping = [
     0,  1
    ]
