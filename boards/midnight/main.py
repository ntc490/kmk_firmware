import board
from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()

# fmt: off
# flake8: noqa
keyboard.keymap = [
    [  # QWERTY
        KC.ENT, KC.J
    ]
]

if __name__ == "__main__":
    keyboard.go()

