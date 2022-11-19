import board
from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()

# fmt: off
# flake8: noqa
keyboard.keymap = [
#    [  # QWERTY - Right
#        KC.Y, KC.U, KC.I, KC.O, KC.P, KC.BACKSLASH,
#        KC.H, KC.J, KC.k, KC.L, KC.SEMICOLON, KC.QUOTE,
#        KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH, KC.LSFT,
#        KC.LALT, KC.ENTER, KC.LCTL,
#    ]
    [  # QWERTY - Left
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T,
        KC.LGUI, KC.A, KC.S, KC.D, KC.F, KC.G,
        KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B,
                             KC.BACKSPACE, KC.LCTL, KC.LALT,
    ]
]

if __name__ == "__main__":
    keyboard.go()

