# Higher level Keyboard config like layers
import board
from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()


# fmt: off
# flake8: noqa
keyboard.keymap = [
    [  # QWERTY - Right
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T,            KC.Y, KC.U, KC.I, KC.O, KC.P, KC.BACKSLASH,
        KC.LGUI, KC.A, KC.S, KC.D, KC.F, KC.G,           KC.H, KC.J, KC.k, KC.L, KC.SEMICOLON, KC.QUOTE,
        KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B,           KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH, KC.LSFT,
                   KC.BACKSPACE, KC.LCTL, KC.LALT,    KC.LALT, KC.ENTER, KC.LCTL,
    ]
]

if __name__ == "__main__":
    keyboard.go()

