import time
import digitalio

DOT = 0.2
DASH = DOT * 3
SYMBOL_SPACE = DOT
LETTER_SPACE = DOT * 3
WORD_SPACE = DOT * 7

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'
}

class MorseBlinker:
    def __init__(self):
        #self.led = digitalio.DigitalInOut(led_pin)
        #self.led.direction = digitalio.Direction.OUTPUT
        self.reset()

    def reset(self):
        self.message = ""
        self.sequence = []
        self.index = 0
        self.next_change = 0
        #self.led.value = False
        self.running = False

    def start(self, text):
        self.message = text.upper()
        self.sequence = self._generate_sequence(self.message)
        self.index = 0
        self.next_change = time.monotonic()
        self.running = True
        print(f"Starting Morse: {self.message}")

    def _generate_sequence(self, text):
        seq = []
        for i, char in enumerate(text):
            if char == ' ':
                seq.append(('pause', WORD_SPACE))
                continue
            morse = MORSE_CODE_DICT.get(char)
            if not morse:
                continue
            for symbol in morse:
                if symbol == '.':
                    seq.append(('on', DOT))
                elif symbol == '-':
                    seq.append(('on', DASH))
                seq.append(('off', SYMBOL_SPACE))
            seq.pop()  # remove trailing symbol space
            seq.append(('pause', LETTER_SPACE))
        return seq

    def during_matrix_scan(self, keyboard):
        print("hooked")
        if not self.running or self.index >= len(self.sequence):
            #self.led.value = False
            print("NTC finished")
            self.running = False
            return

        now = time.monotonic()
        if now < self.next_change:
            return

        action, duration = self.sequence[self.index]

        if action == 'on':
            print("NTC on")
            #self.led.value = True
        else:
            print("NTC off")
            #self.led.value = False

        self.next_change = now + duration
        self.index += 1
