# Higher level Keyboard config like layers
import board
from kb import KMKKeyboard, Mapper
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.modules.oneshot import OneShot
from kmk.modules.mouse_keys import MouseKeys

keyboard = KMKKeyboard()


keyboard.modules.extend([ Layers(), ModTap(), OneShot(), MouseKeys() ])

# --------------- Key aliases ---------------

QWERTY_LAYER = 0
COLEMAK_LAYER = 1
NUM_LAYER = 2
PWR_LAYER = 3
FUNC_LAYER = 4
TAP_TIME = 200

# Simple Key definitions
_______ = KC.TRNS
XXXXXXX = KC.NO
NEXTWIN = KC.LGUI(KC.GRAVE)
C_A_DEL = KC.LCTL(KC.LALT(KC.DEL))
QWERTY = KC.DF(QWERTY_LAYER)
COLEMK = KC.DF(COLEMAK_LAYER)
GUI_T = KC.MT(KC.T, KC.LGUI(KC.T), prefer_hold=False, tap_time=300)
GUI_F = KC.MT(KC.F, KC.LGUI(KC.F), prefer_hold=False, tap_time=300)
GUI_X = KC.MT(KC.X, KC.LGUI(KC.X), prefer_hold=False, tap_time=300)
GUI_C = KC.MT(KC.C, KC.LGUI(KC.C), prefer_hold=False, tap_time=300)
GUI_V = KC.MT(KC.V, KC.LGUI(KC.V), prefer_hold=False, tap_time=300)
GUI_L = KC.MT(KC.L, KC.LGUI(KC.L), prefer_hold=False, tap_time=300)
GUI_M = KC.MT(KC.M, KC.LGUI(KC.M), prefer_hold=False, tap_time=300)

# Fancy mod-tap/layer-tap multi-function keys
LGUI_ENTER = KC.MT(KC.ENTER, KC.LGUI, prefer_hold=True, tap_time=TAP_TIME)
NUM_TAB = KC.LT(NUM_LAYER, KC.TAB, prefer_hold=True, tap_time=TAP_TIME)
PWR_ESC = KC.LT(PWR_LAYER, KC.ESC, prefer_hold=True, tap_time=TAP_TIME)
FUNC_Z = KC.LT(FUNC_LAYER, KC.Z, prefer_hold=False, tap_time=TAP_TIME)
HYPR_SPC = KC.MT(KC.SPACE, KC.HYPR, prefer_hold=False, tap_time=TAP_TIME)

# Left and right shift work normally when held. Left shift tap does a
# one-shot number layer, right shift tap does a one-shot number layer
# with shift (symbols)
RSFTNUM_RSFT = KC.MT(KC.OS(KC.LM(NUM_LAYER, KC.RSFT)), KC.RSFT, prefer_hold=True, tap_time=TAP_TIME)
NUM_LSFT = KC.MT(KC.OS(KC.MO(NUM_LAYER)), KC.LSFT, prefer_hold=True, tap_time=TAP_TIME)

# --------------- Key maps ---------------

qwerty = Mapper()
colemak = Mapper()
numbers = Mapper()
power_user = Mapper()
func_keys = Mapper()

qwerty.left(
    PWR_ESC,    KC.Q,       KC.W,       KC.E,       KC.R,       GUI_T,
    NUM_TAB,    KC.A,       KC.S,       KC.D,       GUI_F,      KC.G,
    NUM_LSFT,   FUNC_Z,     GUI_X,      GUI_C,      GUI_V,      KC.B,
                                                  KC.BACKSPACE, KC.LCTL, KC.LALT
)
qwerty.right(
    KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,         KC.BSLASH,
    KC.H,       KC.J,       KC.K,       GUI_L,      KC.SEMICOLON, KC.QUOTE,
    KC.N,       GUI_M,      KC.COMMA,   KC.DOT,     KC.SLASH,     RSFTNUM_RSFT,
  KC.LALT, LGUI_ENTER, HYPR_SPC,
)

colemak.left(
    PWR_ESC,    KC.Q,       KC.W,       KC.F,       KC.P,       KC.B,
    NUM_TAB,    KC.A,       KC.R,       KC.S,       KC.T,       KC.G,
    NUM_LSFT,   FUNC_Z,     KC.X,       KC.C,       KC.D,       KC.V,
                                                  KC.BACKSPACE, KC.LCTL, KC.LALT,
)
colemak.right(
    KC.J,       KC.L,       KC.U,       KC.Y,       KC.SEMICOLON, KC.BSLASH,
    KC.M,       KC.N,       KC.E,       KC.I,       KC.O,         KC.QUOTE,
    KC.K,       KC.H,       KC.COMMA,   KC.DOT,     KC.SLASH,     RSFTNUM_RSFT,
  KC.LALT, LGUI_ENTER, HYPR_SPC,
)

numbers.left(
    KC.ESC,     XXXXXXX,    XXXXXXX,    KC.LCBR,    KC.RCBR,    KC.TILD,
    _______,    XXXXXXX,    XXXXXXX,    KC.LPRN,    KC.RPRN,    KC.GRV,
    _______,    XXXXXXX,    XXXXXXX,    KC.LBRC,    KC.RBRC,    XXXXXXX,
                                                  _______, _______, _______,
)
numbers.right(
    KC.EQUAL,   KC.N7,      KC.N8,      KC.N9,      KC.UNDS,    _______,
    KC.MINUS,   KC.N4,      KC.N5,      KC.N6,      KC.PLUS,    _______,
    KC.DOT,     KC.N1,      KC.N2,      KC.N3,      KC.SLSH,    _______,
  _______, _______, KC.N0,
)

power_user.left(
    _______,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,
    KC.TAB,     XXXXXXX,    KC.MS_LEFT, KC.MS_UP,   KC.MS_DOWN, KC.MS_RIGHT,
    _______,    XXXXXXX,    XXXXXXX,    XXXXXXX,    KC.MB_LMB,  KC.MB_RMB,
                                                  _______, _______, _______,
)
power_user.right(
    XXXXXXX,    KC.PGDN,    KC.PGUP,    XXXXXXX,    XXXXXXX,    XXXXXXX,
    KC.LEFT,    KC.DOWN,    KC.UP,      KC.RIGHT,   XXXXXXX,    XXXXXXX,
    NEXTWIN,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    _______,
  _______, _______, _______,
)

func_keys.left(
    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,
    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    QWERTY,     COLEMK,
    XXXXXXX,    XXXXXXX,    XXXXXXX,    KC.CAPS,    XXXXXXX,    XXXXXXX,
                                                  _______, _______, _______,
)
func_keys.right(
    KC.HOME,    KC.F7,     KC.F8,      KC.F9,      KC.F10,      KC.DEL,
    KC.END,     KC.F4,     KC.F5,      KC.F6,      KC.F11,      KC.PSCREEN,
    KC.INS,     KC.F1,     KC.F2,      KC.F3,      KC.F12,      C_A_DEL,
  _______, _______, _______,
)

# fmt: off
# flake8: noqa
keyboard.keymap = [
    qwerty.map(),
    colemak.map(),
    numbers.map(),
    power_user.map(),
    func_keys.map()
]

if __name__ == "__main__":
    keyboard.go()

