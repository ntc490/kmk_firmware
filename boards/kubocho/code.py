# Higher level Keyboard config like layers
#
# QWERTY [base layer]
# ,-----.-----.-----.-----.-----.-----.        ,-----.-----.-----.-----.-----.-----.
# | ESC | q   | w   | e   | r   | t   |        | y   | u   | i   | o   | p   | \ | |
# |-----+-----+-----+-----+-----+-----|        |-----+-----+-----+-----+-----+-----|
# | TAB | a * | s * | d * | f * | g   |        | h   | j * | k * | l * | ;:* | ' " |
# |-----+-----+-----+-----+-----+-----+        |-----+-----+-----+-----+-----+-----|
# | SHF | z   | x   | c   | v   | b   |        | n   | m   | , < | . > | / ? | FUNC|
# `-----'-----'-----'-----'-----'-----'        `-----'-----'-----'-----'-----'-----'
#               .-------.-------.-------.    .-------.-------.-------.
#               | BKSP  |  CTR  |  NUMS |    |  NUMS | ENTER |  SPC  |
#               '-------'-------'-------'    '-------'-------'-------'
#
# Numbers
# ,-----.-----.-----.-----.-----.-----.        ,-----.-----.-----.-----.-----.-----.
# |     | ` ~ | XXX | SOS | (   | )   |        | = + | 7 & | 8 * | 9 ( | [ { | ] } |
# |-----+-----+-----+-----+-----+-----|        |-----+-----+-----+-----+-----+-----|
# | CAPS|     |     |     | { * | }   |        | - _ | 4*$ | 5*% | 6*^ | '*" |     |
# |-----+-----+-----+-----+-----+-----+        |-----+-----+-----+-----+-----+-----|
# |     |     |     | ESC | [   | ]   |        | . > | 1 ! | 2 @ | 3 # |     |     |
# `-----'-----'-----'-----'-----'-----'        `-----'-----'-----'-----'-----'-----'
#               .-------.-------.-------.    .-------.-------.-------.
#               |       |       |       |    |       |       |   0 ) |
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
import busio
import time
import adafruit_drv2605
from kb import KMKKeyboard, Mapper42, add_keyboard_layer
from kmk.keys import KC, Key, make_key
from kmk.modules.layers import Layers
from kmk.modules.holdtap import HoldTap, HoldTapRepeat
from kmk.modules.pedometer import Pedometer
from kmk.modules.keeper import Keeper

keyboard = KMKKeyboard()

class DRV2605Extended(adafruit_drv2605.DRV2605):
    """Extended DRV2605 class with is_playing() method."""

    GO_REG = 0x0C  # Register 0x0C holds the GO bit

    def is_playing(self):
        """
        Returns True if a waveform is currently playing.
        Checks the GO bit in register 0x0C.
        """
        go_val = self._read_u8(self.GO_REG)
        return (go_val & 0x01) != 0


class HapticHoldTap(HoldTap):
    def __init__(self):
        super().__init__()
        self.i2c = busio.I2C(board.GP27, board.GP26)
        self.drv = DRV2605Extended(self.i2c)
        self.last_play_time = 0

    def play(self, effect):
        if self.play_lockout():
            return
        self.drv.sequence[0] = adafruit_drv2605.Effect(effect)
        self.drv.sequence[1] = adafruit_drv2605.Effect(0)
        self.drv.play()
        self.last_play_time = time.monotonic()

    def play_lockout(self):
        return (time.monotonic() - self.last_play_time) < 0.7

    def ht_activate_hold(self, key, keyboard, *args, **kwargs):
        STRONG_BUZZ = 14
        self.play(STRONG_BUZZ)
        super().ht_activate_hold(key, keyboard, *args, **kwargs)

    def ht_deactivate_hold(self, key, keyboard, *args, **kwargs):
        STRONG_CLICK = 17
        self.play(STRONG_CLICK)
        super().ht_deactivate_hold(key, keyboard, *args, **kwargs)


holdtap = HapticHoldTap()
holdtap.tap_time = 200
keeper = Keeper()

keyboard.modules.extend([ Layers(), holdtap, Pedometer(), keeper ])

# --------------- Layer Objects ---------------

qwerty = Mapper42()
nums   = Mapper42()
fkeys  = Mapper42()
power  = Mapper42()
#snake  = Mapper42()
#camel  = Mapper42()
#kebab  = Mapper42()

# --------------- Key Definitions and Aliases ---------------

_______ = KC.TRNS
XXXXXXX = KC.NO
NUM_LYR = KC.MO(nums.layer_id)
FKEY_LYR = KC.MO(fkeys.layer_id)
NEXTWIN = KC.LGUI(KC.GRAVE)
PWR_LYR = KC.MO(power.layer_id)
TAB_PWR = KC.HT(KC.TAB, PWR_LYR)

make_key(
    names=('SOS',),
    on_press=lambda *args: print("SOS")
)

# Use GASC for home-row mods
HOME_ROW_OPTS = { 'prefer_hold': False, 'repeat': HoldTapRepeat.TAP }
GUI_A = KC.HT(KC.A, KC.LGUI, group=1, **HOME_ROW_OPTS)
ALT_S = KC.HT(KC.S, KC.LALT, group=1, **HOME_ROW_OPTS)
SHFT_D = KC.HT(KC.D, KC.LSFT, group=1, **HOME_ROW_OPTS)
CTRL_F = KC.HT(KC.F, KC.LCTRL, group=1, **HOME_ROW_OPTS)

CTRL_J = KC.HT(KC.J, KC.RCTRL, group=2, **HOME_ROW_OPTS)
SHFT_K = KC.HT(KC.K, KC.RSFT, group=2, **HOME_ROW_OPTS)
ALT_L = KC.HT(KC.L, KC.LALT, group=2, **HOME_ROW_OPTS)
GUI_SEMI = KC.HT(KC.SEMICOLON, KC.RGUI, group=2, **HOME_ROW_OPTS)

CTRL_4 = KC.HT(KC.N4, KC.RCTRL, group=2, **HOME_ROW_OPTS)
SHFT_5 = KC.HT(KC.N5, KC.RSFT, group=2, **HOME_ROW_OPTS)
ALT_6 = KC.HT(KC.N6, KC.LALT, group=2, **HOME_ROW_OPTS)
GUI_QUOTE = KC.HT(KC.QUOTE, KC.RGUI, group=2, **HOME_ROW_OPTS)

# Home row mods for number layer left-hand
CTRL_LB = KC.HT(KC.LCBR, KC.LCTRL, group=1, **HOME_ROW_OPTS)

# --------------- Key maps ---------------

qwerty.left(
    KC.ESC,     KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,
    TAB_PWR,    GUI_A,      ALT_S,      SHFT_D,     CTRL_F,     KC.G,
    KC.LSFT,    KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,
                                        KC.BKSP,    KC.LCTRL,   NUM_LYR
)

qwerty.right(
    KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,       KC.BSLASH,
    KC.H,       CTRL_J,     SHFT_K,     ALT_L,      GUI_SEMI,   KC.QUOTE,
    KC.N,       KC.M,       KC.COMMA,   KC.DOT,     KC.SLASH,   FKEY_LYR,
    NUM_LYR,    KC.ENTER,   KC.SPACE
)

# Home row mods poke through for all keys on the left-hand side
nums.left(
    _______,    KC.GRAVE,    XXXXXXX,    KC.SOS,    KC.LPRN,    KC.RPRN,
    KC.CAPS,    _______,     _______,    _______,   CTRL_LB,    KC.RCBR,
    _______,    _______,     _______,    KC.ESC,    KC.LBRC,    KC.RBRC,
                                         _______,   _______,    _______,
)

nums.right(
    KC.EQUAL,   KC.N7,      KC.N8,      KC.N9,      KC.LBRC,    KC.RBRC,
    KC.MINUS,   CTRL_4,     SHFT_5,     ALT_6,      GUI_SEMI,   _______,
    KC.DOT,     KC.N1,      KC.N2,      KC.N3,      _______,    _______,
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
