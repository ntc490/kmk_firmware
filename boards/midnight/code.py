# Higher level Keyboard config like layers
import board
from kb import KMKKeyboard, Mapper42, add_keyboard_layer
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.holdtap import HoldTap, HoldTapRepeat

keyboard = KMKKeyboard()

keyboard.modules.extend([ Layers(), HoldTap() ])

# --------------- Layer Indexes ---------------

qwerty = Mapper42()

# --------------- Key Definitions and Aliases ---------------

# Use GASC for home-row mods
GUI_A = KC.HT(KC.A, KC.LGUI, prefer_hold=False, repeat=HoldTapRepeat.TAP)
ALT_S = KC.HT(KC.S, KC.LALT, prefer_hold=False, repeat=HoldTapRepeat.TAP)
SHFT_D = KC.HT(KC.D, KC.LSFT, prefer_hold=False, repeat=HoldTapRepeat.TAP)
CTRL_F = KC.HT(KC.F, KC.LCTRL, prefer_hold=False, repeat=HoldTapRepeat.TAP)

CTRL_J = KC.HT(KC.J, KC.RCTRL, prefer_hold=False,repeat=HoldTapRepeat.TAP)
SHFT_K = KC.HT(KC.K, KC.RSFT, prefer_hold=False, repeat=HoldTapRepeat.TAP)
ALT_L = KC.HT(KC.L, KC.LALT, prefer_hold=False, repeat=HoldTapRepeat.TAP)
GUI_SEMI = KC.HT(KC.SEMICOLON, KC.RGUI, prefer_hold=False, repeat=HoldTapRepeat.TAP)

# --------------- Key maps ---------------

qwerty.left(
    KC.TAB,     KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,
    KC.LCTRL,   GUI_A,      ALT_S,      SHFT_D,     CTRL_F,     KC.G,
    KC.LSFT,    KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,
                                      KC.BKSP,   KC.LCTRL,   KC.LALT
)

qwerty.right(
    KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,         KC.BACKSLASH,
    KC.H,       CTRL_J,     SHFT_K,     ALT_L,      GUI_SEMI,     KC.QUOTE,
    KC.N,       KC.M,       KC.COMMA,   KC.DOT,     KC.SLASH,     KC.RSFT,
    KC.LALT,    KC.ENTER,   KC.SPACE
)

# fmt: off
# flake8: noqa
add_keyboard_layer(keyboard,
                   qwerty)

if __name__ == "__main__":
    keyboard.go()
