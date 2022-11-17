import board
from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()

# fmt: off
# flake8: noqa
keyboard.keymap = [
    [  # QWERTY
        KC.Y, KC.U, KC.I, KC.O, KC.P, KC.BACKSLASH,
        KC.H, KC.J, KC.k, KC.L, KC.SEMICOLON, KC.QUOTE,
        KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH, KC.LSFT,
                              KC.LALT, KC.ENTER, KC.LCTL,
    ]
]

if __name__ == "__main__":
    keyboard.go()

