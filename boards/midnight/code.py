# Higher level Keyboard config like layers
import board
from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.modules.oneshot import OneShot

keyboard = KMKKeyboard()


keyboard.modules.extend([ Layers(), ModTap(), OneShot() ])

# --------------- Key aliases ---------------

QWERTY_LAYER = 0
COLEMAK_LAYER = 1
NUM_LAYER = 2
PWR_LAYER = 3
FUNC_LAYER = 4
MOUSE_LAYER = 5

______ = KC.TRNS
XXXXXX = KC.NO
TAP_TIME = 300
LGUI_ENTER = KC.MT(KC.ENTER, KC.LGUI, prefer_hold=False, tap_time=TAP_TIME)
NUM_TAB = KC.LT(NUM_LAYER, KC.TAB, prefer_hold=True, tap_time=TAP_TIME)
PWR_ESC = KC.LT(PWR_LAYER, KC.ESC, tap_time=TAP_TIME)
FUNC_Z = KC.LT(FUNC_LAYER, KC.Z, prefer_hold=False, tap_time=TAP_TIME)
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
        KC.LSFT, FUNC_Z,  KC.X,    KC.C,    KC.V,    KC.B,             KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH,     KC.OS(KC.LM(NUM_LAYER, KC.LSFT)),
                               KC.BACKSPACE, KC.LCTL, KC.LALT,      KC.LALT, LGUI_ENTER, HYPR_SPC,
    ],
    [  # Colemak
        PWR_ESC, KC.Q,    KC.W,    KC.F,    KC.P,    KC.B,             KC.J, KC.L, KC.U,     KC.Y,   KC.SEMICOLON, KC.BSLASH,
        NUM_TAB, KC.A,    KC.R,    KC.S,    KC.T,    KC.G,             KC.M, KC.N, KC.E,     KC.I,   KC.O,         KC.QUOTE,
        KC.LSFT, FUNC_Z,  KC.X,    KC.C,    KC.D,    KC.V,             KC.K, KC.H, KC.COMMA, KC.DOT, KC.SLASH,     KC.OS(KC.LM(NUM_LAYER, KC.LSFT)),
                               KC.BACKSPACE, KC.LCTL, KC.LALT,      KC.LALT, LGUI_ENTER, HYPR_SPC,
    ],
    [  # Numbers
        KC.ESC,  XXXXXX,  XXXXXX, XXXXXX, KC.LCBR, KC.RCBR,            KC.EQUAL, KC.N7, KC.N8, KC.N9, KC.UNDS,  ______,
        ______,  XXXXXX,  XXXXXX, KC.TILD,KC.LPRN, KC.RPRN,            KC.MINUS, KC.N4, KC.N5, KC.N6, KC.PLUS,  ______,
        ______,  XXXXXX,  XXXXXX, KC.GRV, KC.LBRC, KC.RBRC,            KC.DOT,   KC.N1, KC.N2, KC.N3, KC.SLSH,  ______,
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
        XXXXXX,  XXXXXX,  XXXXXX, XXXXXX, KC.DF(QWERTY_LAYER), KC.DF(COLEMAK_LAYER),              KC.END,   KC.F4,   KC.F5,  KC.F6,  KC.F11,  KC.PSCREEN,
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

