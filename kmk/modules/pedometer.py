from micropython import const

from kmk.modules import Module
from kmk.utils import Debug

debug = Debug(__name__)


class Pedometer(Module):
    def __init__(self):
        self.key_count = 0

    def during_bootup(self, keyboard):
        return

    def before_matrix_scan(self, keyboard):
        return

    def after_matrix_scan(self, keyboard):
        return

    def process_key(self, keyboard, key, is_pressed, int_coord):
        '''Simply count the number of keys pressed so we can keep track of how
        much we've worked our hands.'''
        if is_pressed:
            self.key_count += 1
            debug(f'Adding another key press {self.key_count}')
        return key

    def before_hid_send(self, keyboard):
        return

    def after_hid_send(self, keyboard):
        return

    def on_powersave_enable(self, keyboard):
        return

    def on_powersave_disable(self, keyboard):
        return
