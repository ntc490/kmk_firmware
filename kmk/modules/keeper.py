from micropython import const

from kmk.keys import KC, make_argumented_key
from kmk.modules import Module
from kmk.utils import Debug

debug = Debug(__name__)


class Keeper(Module):
    """Jiggler to keep 'here' status at bay"""
    def __init__(self):
        self.timeout_ms = 60 * 1000
        self.timer = None
        self.enabled = False

    def during_bootup(self, keyboard):
        return

    def before_matrix_scan(self, keyboard):
        return

    def after_matrix_scan(self, keyboard):
        return

    def process_key(self, keyboard, key, is_pressed, int_coord):
        '''Reset the keeper timer so we arent tickling the computer.'''
        if self.enabled:
            self.reset_timer(keyboard)
        return key

    def before_hid_send(self, keyboard):
        return

    def after_hid_send(self, keyboard):
        return

    def on_powersave_enable(self, keyboard):
        return

    def on_powersave_disable(self, keyboard):
        return

    def reset_timer(self, keyboard):
        if self.timer is not None:
            keyboard.cancel_timeout(self.timer)
        self.timer = keyboard.set_timeout(self.timeout_ms, lambda: self.on_timeout(keyboard))

    def on_timeout(self, keyboard):
        debug('timed out')
        if not self.enabled:
            return
        debug('reset and press shift')
        self.reset_timer(keyboard)
        # Send a shift key press and release
        keyboard.tap_key(KC.LSFT)

    def enable(self, state):
        self.enabled = state
