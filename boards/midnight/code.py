# Higher level Keyboard config like layers
#
# Keymappings adapted from:
# https://peterxjang.com/blog/designing-a-36-key-custom-keyboard-layout.html
#
# QWERTY [base layer]
# ,-----.-----.-----.-----.-----.                      ,-----.-----.-----.-----.-----.
# | Q   | W   | E   | R   | T   |                      | Y   | U   | I   | O   | P   |
# |-----+-----+-----+-----+-----|                      |-----+-----+-----+-----+-----|
# | A   | S   | D   | F   | G   |                      | H   | J   | K   | L   | ; : |
# |-----+-----+-----+-----+-----+                      |-----+-----+-----+-----+-----|
# |SHF/Z| X   | C   | V   | B   |                      | N   | M   | , < | . > |SHF/?|
# `-----'-----'-----'-----'-----'                      `-----'-----'-----'-----'-----'
#               .-------.-------.-------.      .-------.-------.-------.
#               |GUI/ESC|CTR/TAB|ALT/OSN|      |FKY/BSP|NUM/ENT|HYP/SPC|
#               '-------'-------'-------'      '-------'-------'-------'
#
# Colemak [base layer]
# ,-----.-----.-----.-----.-----.                      ,-----.-----.-----.-----.-----.
# | Q   | W   | F   | P   | B   |                      | J   | L   | U   | Y   | ; : |
# |-----+-----+-----+-----+-----|                      |-----+-----+-----+-----+-----|
# | A   | R   | S   | T   | G   |                      | M   | N   | E   | I   | O   |
# |-----+-----+-----+-----+-----+                      |-----+-----+-----+-----+-----|
# |SHF/Z| X   | C   | D   | V   |                      | K   | H   | , < | . > |SHF/?|
# `-----'-----'-----'-----'-----'                      `-----'-----'-----'-----'-----'
#               .-------.-------.-------.      .-------.-------.-------.
#               |GUI/ESC|CTR/TAB|ALT/OSN|      |FKY/BSP|NUM/ENT|HYP/SPC|
#               '-------'-------'-------'      '-------'-------'-------'
#
# Numbers
# ,-----.-----.-----.-----.-----.                      ,-----.-----.-----.-----.-----.
# | 1!  | 2@  | 3#  | 4$  | 5%  |                      | 6^  | 7&  | 8*  | 9(  | 0)  |
# |-----+-----+-----+-----+-----|                      |-----+-----+-----+-----+-----|
# | `~  |HOME |PGUP |PGDN | END |                      |LEFT |DOWN | UP  |RGHT | ' " |
# |-----+-----+-----+-----+-----+                      |-----+-----+-----+-----+-----|
# |SHFT | = + | - _ | [ { | ] } |                      |NXTWN| RET |LKUP |     |SHF\||
# `-----'-----'-----'-----'-----'                      `-----'-----'-----'-----'-----'
#               .-------.-------.-------.      .-------.-------.-------.
#               |       |       |       |      | BKSP  |(hold) |       |
#               '-------'-------'-------'      '-------'-------'-------'
#
# Function keys
# ,-----.-----.-----.-----.-----.                      ,-----.-----.-----.-----.-----.
# | F1  | F2  | F3  | F4  | F5  |                      | F6  | F7  | F8  | F9  | F10 |
# |-----+-----+-----+-----+-----|                      |-----+-----+-----+-----+-----|
# | F11 | F12 | XXX | XXX | XXX |                      |MLEFT|MDOWN| MUP |MRGHT| XXX |
# |-----+-----+-----+-----+-----+                      |-----+-----+-----+-----+-----|
# | SHFT| XXX |CAPS |QWERT|COLEM|                      |BTN1 | BTN2| XXX | XXX |SHFT |
# `-----'-----'-----'-----'-----'                      `-----'-----'-----'-----'-----'
#               .-------.-------.-------.      .-------.-------.-------.
#               |       |       |       |      |(hold) |       | SPACE |
#               '-----------------------'      '-------'-------'-------'
#
# Snake
# ,-----.-----.-----.-----.-----.                      ,-----.-----.-----.-----.-----.
# |     |     |     |     |     |                      |     |     |     |     |     |
# |-----+-----+-----+-----+-----|                      |-----+-----+-----+-----+-----|
# |     |     |     |     |     |                      |     |     |     |     |     |
# |-----+-----+-----+-----+-----+                      |-----+-----+-----+-----+-----|
# |     |     |     |     |     |                      |     |     |     |     |     |
# `-----'-----'-----'-----'-----'                      `-----'-----'-----'-----'-----'
#               .-------.-------.-------.      .-------.-------.-------.
#               |       |       |       |      | EXIT  |       |  UNDS |
#               '-----------------------'      '-------'-------'-------'
#
# Camel
# ,-----.-----.-----.-----.-----.                      ,-----.-----.-----.-----.-----.
# |     |     |     |     |     |                      |     |     |     |     |     |
# |-----+-----+-----+-----+-----|                      |-----+-----+-----+-----+-----|
# |     |     |     |     |     |                      |     |     |     |     |     |
# |-----+-----+-----+-----+-----+                      |-----+-----+-----+-----+-----|
# |     |     |     |     |     |                      |     |     |     |     |     |
# `-----'-----'-----'-----'-----'                      `-----'-----'-----'-----'-----'
#               .-------.-------.-------.      .-------.-------.-------.
#               |       |       |       |      | EXIT  |       |OS(SFT)|
#               '-----------------------'      '-------'-------'-------'
#
# Kebab
# ,-----.-----.-----.-----.-----.                      ,-----.-----.-----.-----.-----.
# |     |     |     |     |     |                      |     |     |     |     |     |
# |-----+-----+-----+-----+-----|                      |-----+-----+-----+-----+-----|
# |     |     |     |     |     |                      |     |     |     |     |     |
# |-----+-----+-----+-----+-----+                      |-----+-----+-----+-----+-----|
# |     |     |     |     |     |                      |     |     |     |     |     |
# `-----'-----'-----'-----'-----'                      `-----'-----'-----'-----'-----'
#               .-------.-------.-------.      .-------.-------.-------.
#               |       |       |       |      | EXIT  |       | MINUS |
#               '-----------------------'      '-------'-------'-------'

import board
from kb import KMKKeyboard, Mapper36
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.modules.oneshot import OneShot
from kmk.modules.mouse_keys import MouseKeys

keyboard = KMKKeyboard()

keyboard.modules.extend([ Layers(), ModTap(), OneShot(), MouseKeys() ])

# --------------- Layer Indexes ---------------

qwerty = Mapper36()
colemak = Mapper36()
numbers = Mapper36()
fkeys = Mapper36()
snake = Mapper36()
camel = Mapper36()
kebab = Mapper36()

# --------------- Key Definitions and Aliases ---------------

_______ = KC.TRNS
XXXXXXX = KC.NO
NEXTWIN = KC.LGUI(KC.GRAVE)
QWERTY = KC.DF(qwerty.layer_id)
COLEMAK = KC.DF(colemak.layer_id)
RET = KC.LALT(KC.ASTR)
LKUP = KC.LALT(KC.DOT)
GUI_T = KC.MT(KC.T, KC.LGUI(KC.T), prefer_hold=False, tap_time=300)
GUI_X = KC.MT(KC.X, KC.LGUI(KC.X), prefer_hold=False, tap_time=300)
GUI_C = KC.MT(KC.C, KC.LGUI(KC.C), prefer_hold=False, tap_time=300)
GUI_V = KC.MT(KC.V, KC.LGUI(KC.V), prefer_hold=False, tap_time=300)
GUI_M = KC.MT(KC.M, KC.LGUI(KC.M), prefer_hold=False, tap_time=300)
SNAKE_TG = KC.TG(snake.layer_id)
CAMEL_TG = KC.TG(camel.layer_id)
KEBAB_TG = KC.TG(kebab.layer_id)

# Fancy mod-tap/layer-tap multi-function keys
SHIFT_Z = KC.MT(KC.Z, KC.LSFT, prefer_hold=True)
SHIFT_SLASH = KC.MT(KC.SLASH, KC.RSFT, prefer_hold=True)
SHIFT_BACKSLASH = KC.MT(KC.BACKSLASH, KC.RSFT, prefer_hold=True)
LGUI_ESC = KC.MT(KC.ESC, KC.LGUI, prefer_hold=True)
CTRL_TAB = KC.MT(KC.TAB, KC.LCTRL, prefer_hold=True)
ALT_OSNUM = KC.MT(KC.OS(KC.MO(numbers.layer_id)), KC.LALT, prefer_hold=True)
NUM_ENTER = KC.LT(numbers.layer_id, KC.ENTER, prefer_hold=True)
HYPR_SPACE = KC.MT(KC.SPACE, KC.HYPR, prefer_hold=False)
FKEY_BKSP = KC.LT(fkeys.layer_id, KC.BKSP, prefer_hold=False)

# --------------- Key maps ---------------

qwerty.left(
    KC.Q,       KC.W,       KC.E,       KC.R,       GUI_T,
    KC.A,       KC.S,       KC.D,       KC.F,       KC.G,
    SHIFT_Z,    GUI_X,      GUI_C,      GUI_V,      KC.B,
                            LGUI_ESC,   CTRL_TAB,   ALT_OSNUM
)
qwerty.right(
    KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,
    KC.H,       KC.J,       KC.K,       KC.L,       KC.SEMICOLON,
    KC.N,       GUI_M,      KC.COMMA,   KC.DOT,     SHIFT_SLASH,
    FKEY_BKSP,  NUM_ENTER,  HYPR_SPACE
)

colemak.left(
    KC.Q,       KC.W,       KC.F,       KC.P,       KC.B,
    KC.A,       KC.R,       KC.S,       KC.T,       KC.G,
    SHIFT_Z,    KC.X,       KC.C,       KC.D,       KC.V,
                            LGUI_ESC,   CTRL_TAB,   ALT_OSNUM
)
colemak.right(
    KC.J,       KC.L,       KC.U,       KC.Y,       KC.SEMICOLON,
    KC.M,       KC.N,       KC.E,       KC.I,       KC.O,
    KC.K,       KC.H,       KC.COMMA,   KC.DOT,     SHIFT_SLASH,
    FKEY_BKSP,  NUM_ENTER,  HYPR_SPACE
)

numbers.left(
    KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5,
    KC.TILD,    KC.HOME,    KC.PGUP,    KC.PGDN,    KC.END,
    KC.LSFT,    KC.EQUAL,   KC.MINUS,   KC.LBRC,    KC.RBRC,
                            _______,    _______,    _______
)
numbers.right(
    KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0,
    KC.LEFT,    KC.DOWN,    KC.UP,      KC.RIGHT,   KC.QUOTE,
    NEXTWIN,    SNAKE_TG,   CAMEL_TG,   KEBAB_TG,   SHIFT_BACKSLASH,
    KC.BKSP,    _______,    _______
)

fkeys.left(
    KC.F1,      KC.F2,      KC.F3,      KC.F4,      KC.F5,
    KC.F11,     KC.F12,     XXXXXXX,    XXXXXXX,    XXXXXXX,
    KC.LSFT,    XXXXXXX,    KC.CAPS,    QWERTY,     COLEMAK,
                            _______,    _______,    _______
)
fkeys.right(
    KC.F6,      KC.F7,     KC.F8,      KC.F9,      KC.F10,
    KC.MS_LEFT, KC.MS_DOWN,KC.MS_UP,   KC.MS_RIGHT,XXXXXXX,
    KC.MB_LMB,  KC.MB_RMB, XXXXXXX,    XXXXXXX,    KC.RSFT,
    _______,    _______,   KC.SPACE
)

# Change space to underscore - exit with ESC
snake.left(
    _______,    _______,    _______,    _______,    _______,
    _______,    _______,    _______,    _______,    _______,
    _______,    _______,    _______,    _______,    _______,
                            SNAKE_TG,   _______,  _______
)
snake.right(
    _______,    _______,    _______,    _______,    _______,
    _______,    _______,    _______,    _______,    _______,
    _______,    _______,    _______,    _______,    _______,
    _______,    _______,    KC.UNDS
)

# Change space to one-shot shift - exit with ESC. Note: 'z' key
# doesn't work because of MT on 'z' key.
camel.left(
    _______,    _______,    _______,    _______,    KC.T,
    _______,    _______,    _______,    _______,    _______,
    _______,    KC.X,       KC.C,       KC.V,       _______,
                            CAMEL_TG,   _______,    _______
)
camel.right(
    _______,    _______,    _______,    _______,    _______,
    _______,    _______,    _______,    _______,    _______,
    _______,    KC.M,       _______,    _______,    _______,
    _______,    _______,    KC.OS(KC.LSFT)
)

# Change space to dash - exit with ESC
kebab.left(
    _______,    _______,    _______,    _______,    _______,
    _______,    _______,    _______,    _______,    _______,
    _______,    _______,    _______,    _______,    _______,
                            KEBAB_TG,   _______,  _______
)
kebab.right(
    _______,    _______,    _______,    _______,    _______,
    _______,    _______,    _______,    _______,    _______,
    _______,    _______,    _______,    _______,    _______,
    _______,    _______,    KC.MINUS
)

# fmt: off
# flake8: noqa
keyboard.keymap = [
    qwerty.map(),
    colemak.map(),
    numbers.map(),
    fkeys.map(),
    snake.map(),
    camel.map(),
    kebab.map()
]

if __name__ == "__main__":
    keyboard.go()
