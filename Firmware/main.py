import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()
macros = Macros()
encoder_handler = EncoderHandler()

keyboard.modules.append(macros)
keyboard.modules.append(encoder_handler)


PINS = [
    board.D1, board.D4, board.D7, board.D8, board.D9, board.D10, board.D11
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

encoder_handler.pins = (
    (board.D3, board.D2, None, False), 
    (board.D6, board.D5, None, False), 
)

keyboard.keymap = [
    [
        KC.ENTER,          
        KC.NO,             
        KC.LCTL(KC.Z),     
        KC.LCTL(KC.C),     
        KC.LCTL(KC.V),     
        KC.LCTL(KC.PPLS),  
        KC.LCTL(KC.PMNS), 
    ]
]

encoder_handler.map = [
    ((KC.LCTL(KC.PPLS), KC.LCTL(KC.PMNS)),), 
    ((KC.VOLU, KC.VOLD),),                   
    
]

if __name__ == '__main__':
    keyboard.go()
