# Higher level Keyboard config like layers
#
# Keymappings adapted from:
# https://peterxjang.com/blog/designing-a-36-key-custom-keyboard-layout.html
#
# QWERTY [base layer]
# ,-----.-----.-----.-----.-----.-----.                      ,-----.-----.-----.-----.-----.-----.
# | TAB | q   | w   | e   | r   | t   |                      | y   | u   | i   | o   | p   | \ | |
# |-----+-----+-----+-----+-----+-----|                      |-----+-----+-----+-----+-----+-----|
# | NC  | a   | s   | d   | f   | g   |                      | h   | j   | k   | l   | ; : | ' " |
# |-----+-----+-----+-----+-----+-----+                      |-----+-----+-----+-----+-----+-----|
# | LSFT| z   | x   | c   | v   | b   |                      | n   | m   | , < | . > | / ? | RSFT|
# `-----.-----'-----'-----'-----'-----'                      `-----'-----'-----'-----'-----+-----'
#               .-------.-------.-------.      .-------.-------.-------.
#               | BKSPC |  CTRL | ALT   |      |  ALT  | ENTER |  SPC  |
#               '-------'-------'-------'      '-------'-------'-------'
#

import board
from kb import KMKKeyboard, Mapper42, add_keyboard_layer
from kmk.keys import KC
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()

#keyboard.modules.extend([ Layers(), ])

# --------------- Layer Indexes ---------------

qwerty = Mapper42()

# --------------- Key Definitions and Aliases ---------------


# --------------- Key maps ---------------

keyboard.keymap = [
[
    KC.TAB,  KC.Q, KC.W, KC.E, KC.R, KC.T,        KC.Y, KC.U, KC.I, KC.O, KC.P,         KC.BACKSLASH,
    KC.NO,   KC.A, KC.S, KC.D, KC.F, KC.G,        KC.H, KC.J, KC.K, KC.L, KC.SEMICOLON, KC.QUOTE,
    KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B,        KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH, KC.RSHIFT,
          KC.BACKSPACE, KC.LCTRL, KC.LALT,        KC.RALT, KC.ENTER, KC.SPACE
]
]

# fmt: off
# flake8: noqa
#add_keyboard_layer(keyboard,
#                   qwerty,)

if __name__ == "__main__":
    keyboard.go()
