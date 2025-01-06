# Higher level Keyboard config like layers
import board
from kb import KMKKeyboard, Mapper42, add_keyboard_layer
from kmk.keys import KC
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()

#keyboard.modules.extend([ Layers() ])

# --------------- Layer Indexes ---------------

qwerty = Mapper42()

# --------------- Key Definitions and Aliases ---------------

# --------------- Key maps ---------------

qwerty.left(
    KC.TAB,     KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,
    KC.LCTRL,   KC.A,       KC.S,       KC.D,       KC.F,       KC.G,
    KC.LSFT,    KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,
                                      KC.BKSP,   KC.LCTRL,   KC.LALT
)
qwerty.right(
    KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,         KC.BACKSLASH,
    KC.H,       KC.J,       KC.K,       KC.L,       KC.SEMICOLON, KC.QUOTE,
    KC.N,       KC.M,       KC.COMMA,   KC.DOT,     KC.SLASH,     KC.RSFT,
    KC.LALT,    KC.ENTER,   KC.SPACE
)

# fmt: off
# flake8: noqa
add_keyboard_layer(keyboard,
                   qwerty)

if __name__ == "__main__":
    keyboard.go()
