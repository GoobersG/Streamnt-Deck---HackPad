import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

# --- Buttons ---
# [SW1, SW3, SW5]
# [SW2, SW4, SW6]
PINS = [
    board.GP26,  # SW1
    board.GP1,   # SW3
    board.GP3,   # SW5

    board.GP2,   # SW2
    board.GP27,  # SW4
    board.GP4,   # SW6
]


keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [
        KC.A, KC.B, KC.C,
        KC.D, KC.E, KC.F,
    ]
]

# --- Encoder ---
# EC11: A and B to GPIOs, C to GND
encoder = EncoderHandler()
keyboard.modules.append(encoder)

# Encoder pins: (A, B)
encoder.pins = ((board.GP28, board.GP29),)

# What rotation does: (CCW, CW)
# Pick one:
# encoder.map = (((KC.VOLD, KC.VOLU),),)      # Volume
encoder.map = (((KC.LEFT, KC.RIGHT),),)       # Arrows

if __name__ == '__main__':
    keyboard.go()
