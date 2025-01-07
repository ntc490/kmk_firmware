# Higher level Keyboard config like layers
#
# QWERTY [base layer]
# ,-----.-----.-----.-----.-----.-----.        ,-----.-----.-----.-----.-----.-----.
# | TAB | q   | w   | e   | r   | t   |        | y   | u   | i   | o   | p   | XXX |
# |-----+-----+-----+-----+-----+-----|        |-----+-----+-----+-----+-----+-----|
# | PWR | a * | s * | d * | f * | g   |        | h   | j * | k * | l * | ;:* | ' " |
# |-----+-----+-----+-----+-----+-----+        |-----+-----+-----+-----+-----+-----|
# | SHF | z   | x   | c   | v   | b   |        | n   | m   | , < | . > | / ? | XXX |
# `-----'-----'-----'-----'-----'-----'        `-----'-----'-----'-----'-----'-----'
#               .-------.-------.-------.    .-------.-------.-------.
#               | BKSP  |  CTR  |  NUMS |    |  NUMS | ENTER |  SPC  |
#               '-------'-------'-------'    '-------'-------'-------'
#
# Numbers
# ,-----.-----.-----.-----.-----.-----.        ,-----.-----.-----.-----.-----.-----.
# | XXX | ` ~ | XXX | XXX | (   | )   |        | = + | 7 & | 8 * | 9 ( | \ | | XXX |
# |-----+-----+-----+-----+-----+-----|        |-----+-----+-----+-----+-----+-----|
# | XXX |     |     |     | {   | }   |        | - _ | 4 $ | 5 % | 6 ^ | ' " | ' " |
# |-----+-----+-----+-----+-----+-----+        |-----+-----+-----+-----+-----+-----|
# |     | XXX | XXX | ESC | [   | ]   |        | . > | 1 ! | 2 @ | 3 # | XXX | XXX |
# `-----'-----'-----'-----'-----'-----'        `-----'-----'-----'-----'-----'-----'
#               .-------.-------.-------.    .-------.-------.-------.
#               |       |       |       |    |       |       |   0   |
#               '-------'-------'-------'    '-------'-------'-------'
#
# F-Keys
# ,-----.-----.-----.-----.-----.-----.        ,-----.-----.-----.-----.-----.-----.
# |     |     |     |     |     |     |        | F10 | F7  | F8  | F9  | F13 | XXX |
# |-----+-----+-----+-----+-----+-----|        |-----+-----+-----+-----+-----+-----|
# |     |     |     |     |     |     |        | F11 | F4  | F5  | F6  | F14 | XXX |
# |-----+-----+-----+-----+-----+-----+        |-----+-----+-----+-----+-----+-----|
# |     |     |     |     |     |     |        | F12 | F1  | F2  | F3  | F15 | XXX |
# `-----'-----'-----'-----'-----'-----'        `-----'-----'-----'-----'-----'-----'
#               .-------.-------.-------.    .-------.-------.-------.
#               |       |       |       |    |       |       |       |
#               '-------'-------'-------'    '-------'-------'-------'
#
# Power-user
# ,-----.-----.-----.-----.-----.-----.        ,-----.-----.-----.-----.-----.-----.
# |     |     |     |     |     |     |        | PGDN| PGUP|     |     |     |     |
# |-----+-----+-----+-----+-----+-----|        |-----+-----+-----+-----+-----+-----|
# |     |     |     |     |     |     |        | <-- | DWN | UP  | --> |     |     |
# |-----+-----+-----+-----+-----+-----+        |-----+-----+-----+-----+-----+-----|
# |     |     |     |     |     |     |        | NXT |     |     |     |     |     |
# `-----'-----'-----'-----'-----'-----'        `-----'-----'-----'-----'-----'-----'
#               .-------.-------.-------.    .-------.-------.-------.
#               |       |       |       |    |       |       |       |
#               '-------'-------'-------'    '-------'-------'-------'


import board
from kb import KMKKeyboard, Mapper42, add_keyboard_layer
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.holdtap import HoldTap, HoldTapRepeat

keyboard = KMKKeyboard()

keyboard.modules.extend([ Layers(), HoldTap() ])

# --------------- Layer Objects ---------------

qwerty = Mapper42()
nums   = Mapper42()
fkeys  = Mapper42() # TODO: No way to activate yet
power  = Mapper42()
#snake  = Mapper42()
#camel  = Mapper42()
#kebab  = Mapper42()

# --------------- Key Definitions and Aliases ---------------

_______ = KC.TRNS
XXXXXXX = KC.NO
NUM_LYR = KC.MO(nums.layer_id)
NEXTWIN = KC.LGUI(KC.GRAVE)
PWR_LYR = KC.MO(power.layer_id)

# Use GASC for home-row mods
GUI_A = KC.HT(KC.A, KC.LGUI, prefer_hold=False, repeat=HoldTapRepeat.TAP)
ALT_S = KC.HT(KC.S, KC.LALT, prefer_hold=False, repeat=HoldTapRepeat.TAP)
SHFT_D = KC.HT(KC.D, KC.LSFT, prefer_hold=False, repeat=HoldTapRepeat.TAP)
CTRL_F = KC.HT(KC.F, KC.LCTRL, prefer_hold=False, repeat=HoldTapRepeat.TAP)

CTRL_J = KC.HT(KC.J, KC.RCTRL, prefer_hold=False, repeat=HoldTapRepeat.TAP)
SHFT_K = KC.HT(KC.K, KC.RSFT, prefer_hold=False, repeat=HoldTapRepeat.TAP)
ALT_L = KC.HT(KC.L, KC.LALT, prefer_hold=False, repeat=HoldTapRepeat.TAP)
GUI_SEMI = KC.HT(KC.SEMICOLON, KC.RGUI, prefer_hold=False, repeat=HoldTapRepeat.TAP)


# --------------- Key maps ---------------

qwerty.left(
    KC.TAB,     KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,
    PWR_LYR,    GUI_A,      ALT_S,      SHFT_D,     CTRL_F,     KC.G,
    KC.LSFT,    KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,
                                        KC.BKSP,    KC.LCTRL,   NUM_LYR
)

qwerty.right(
    KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,       XXXXXXX,
    KC.H,       CTRL_J,     SHFT_K,     ALT_L,      GUI_SEMI,   KC.QUOTE,
    KC.N,       KC.M,       KC.COMMA,   KC.DOT,     KC.SLASH,   XXXXXXX,
    NUM_LYR,    KC.ENTER,   KC.SPACE
)

# Need home-row mods on this layer, too?
# Can we put tab and esc under strong fingers?
nums.left(
    XXXXXXX,    KC.GRAVE,    XXXXXXX,    XXXXXXX,   KC.LPRN,    KC.RPRN,
    XXXXXXX,    _______,     _______,    _______,   KC.LCBR,    KC.RCBR,
    _______,    KC.CAPS,     KC.TAB,     KC.ESC,    KC.LBRC,    KC.RBRC,
                                         _______,   _______,    _______,
)

nums.right(
    KC.EQUAL,   KC.N7,      KC.N8,      KC.N9,      KC.BSLASH,  XXXXXXX,
    KC.MINUS,   KC.N4,      KC.N5,      KC.N6,      KC.QUOTE,   XXXXXXX,
    KC.DOT,     KC.N1,      KC.N2,      KC.N3,      XXXXXXX,    XXXXXXX,
    _______,    _______,    KC.N0
)

fkeys.left(
    _______,    _______,    _______,    _______,    _______,    _______,
    _______,    _______,    _______,    _______,    _______,    _______,
    _______,    _______,    _______,    _______,    _______,    _______,
    _______,    _______,    _______
)

fkeys.right(
    KC.F10,     KC.F7,      KC.F8,      KC.F9,      KC.F13,     XXXXXXX,
    KC.F11,     KC.F4,      KC.F5,      KC.F6,      KC.F14,     XXXXXXX,
    KC.F12,     KC.F1,      KC.F2,      KC.F3,      KC.F15,     XXXXXXX,
    _______,    _______,    _______
)

power.left(
    _______,    _______,    _______,    _______,    _______,    _______,
    _______,    _______,    _______,    _______,    _______,    _______,
    _______,    _______,    _______,    _______,    _______,    _______,
                                        _______,    _______,    _______
)

power.right(
    KC.PGDN,    KC.PGUP,    _______,    _______,    _______,    _______,
    KC.LEFT,    KC.DOWN,    KC.UP,      KC.RIGHT,   _______,    _______,
    NEXTWIN,    _______,    _______,    _______,    _______,    _______,
    _______,    _______,    _______
)

# fmt: off
# flake8: noqa
add_keyboard_layer(keyboard,
                   qwerty,
                   nums,
                   fkeys,
                   power)

if __name__ == "__main__":
    keyboard.go()
