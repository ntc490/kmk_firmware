# Higher level Keyboard config like layers
import board
from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap

keyboard = KMKKeyboard()


keyboard.modules.extend([ Layers(), ModTap() ])

# --------------- Key aliases ---------------

______ = KC.TRNS
XXXXXX = KC.NO
TAP_TIME = 100
LGUI_BS = KC.MT(KC.BACKSPACE, KC.LGUI, prefer_hold=False, tap_time=TAP_TIME)
NUM_TAB = KC.LT(1, KC.TAB, prefer_hold=True, tap_time=TAP_TIME)
PWR_ESC = KC.LT(2, KC.ESC, tap_time=TAP_TIME)
FUNC_Z = KC.LT(3, KC.Z, prefer_hold=False, tap_time=(TAP_TIME*2))
HYPR_SPC = KC.MT(KC.SPACE, KC.HYPR, prefer_hold=False, tap_time=TAP_TIME)
# TODO: Use a mod-tap or layer-tap on ENTER as well?
NEXTWIN = KC.LALT(KC.TILD)
C_A_DEL = KC.LCTL(KC.LALT(KC.DEL))

# --------------- Key maps ---------------

# fmt: off
# flake8: noqa
keyboard.keymap = [
    [  # QWERTY
        PWR_ESC, KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,             KC.Y, KC.U, KC.I,     KC.O,   KC.P,         KC.BSLASH,
        NUM_TAB, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,             KC.H, KC.J, KC.K,     KC.L,   KC.SEMICOLON, KC.QUOTE,
        KC.LSFT, FUNC_Z,  KC.X,    KC.C,    KC.V,    KC.B,             KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH,     KC.RSFT,
                                    LGUI_BS, KC.LCTL, KC.LALT,      KC.LALT, KC.ENTER, HYPR_SPC,
    ],
    [  # Numbers
        KC.ESC,  XXXXXX,  XXXXXX, XXXXXX, KC.LCBR, KC.RCBR,            KC.EQUAL, KC.N7, KC.N8, KC.N9, KC.MINUS, ______,
        ______,  KC.TILD, XXXXXX, XXXXXX, KC.LPRN, KC.RPRN,            KC.MINUS, KC.N4, KC.N5, KC.N6, KC.PLUS,  ______,
        ______,  KC.GRV,  XXXXXX, XXXXXX, KC.LBRC, KC.RBRC,            KC.DOT,   KC.N1, KC.N2, KC.N3, KC.SLSH,  ______,
                                        ______, ______, ______,    ______, ______, KC.N0,
    ],
    [  # Power User
        ______,  ______,  ______, ______, ______,  ______,             ______,  ______,  ______, ______,  ______,  ______,
        KC.TAB,  ______,  ______, ______, ______,  ______,             KC.LEFT, KC.DOWN, KC.UP,  KC.RIGHT,______,  ______,
        ______,  ______,  ______, ______, ______,  ______,             NEXTWIN, ______,  ______, ______,  ______,  ______,
                                        ______, ______, ______,    ______, ______, ______,
    ],
    [  # Function keys
        XXXXXX,  XXXXXX,  XXXXXX, XXXXXX, XXXXXX, XXXXXX,              KC.HOME,  KC.F7,   KC.F8,  KC.F9,  KC.F10,  KC.DEL,
        XXXXXX,  XXXXXX,  XXXXXX, XXXXXX, XXXXXX, XXXXXX,              KC.END,   KC.F4,   KC.F5,  KC.F6,  KC.F11,  KC.PSCREEN,
        XXXXXX,  XXXXXX,  XXXXXX, KC.CAPS,XXXXXX, XXXXXX,              KC.INS,   KC.F1,   KC.F2,  KC.F3,  KC.F12,  C_A_DEL,
                                        ______, ______, ______,    ______, ______, ______,
    ],
    [  # Mouse Layer
        ______,  ______,  ______, ______, ______,  ______,            ______,  ______,  ______, ______,  ______,  ______,
        ______,  ______,  ______, ______, ______,  ______,            ______,  ______,  ______, ______,  ______,  ______,
        ______,  ______,  ______, ______, ______,  ______,            ______,  ______,  ______, ______,  ______,  ______,
                                        ______, ______, ______,    ______, ______, ______,
    ]
]

if __name__ == "__main__":
    keyboard.go()

