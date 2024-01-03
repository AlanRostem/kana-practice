import json
import random
import sys
import keyboard
import time

CONTROLS_TEXT = """Controls:
    <space>: reveal hiragana
    <enter>: random roman"""

class Practice():
    def __init__(self, ex):
        self.r = 0
        self.ex = ex

    def randomize(self):
        self.r = int(random.random() * len(self.ex["roman"]))

    def get_hiragana(self):
        return self.ex["hiragana"][self.r]

    def get_roman(self):
        return self.ex["roman"][self.r]

if __name__ == "__main__":
    file = open("hiragana.json", mode="r", encoding="utf-8")
    content = str(file.read())
    
    data_obj = json.loads(content)

    confident = data_obj["confident"]
    new = data_obj["new"]

    i = input("Revision of all or practice new? (r/n): ")
    i = i.lower()
    while i != "r" and i != "n":
        i = input("Invalid input (r/n): ")

    p = Practice(confident if i == "r" else new)

    sys.stdout.write(f"{CONTROLS_TEXT}\n\n")

    def random_roman(_):
        p.randomize()

        sys.stdout.flush()
        sys.stdout.write(f"\r{p.get_roman()}    ")
        
    def reveal_hiragana(_):
        sys.stdout.flush()
        sys.stdout.write(f"\r{p.get_hiragana()}    ")

    keyboard.on_press_key("enter", random_roman)
    keyboard.on_press_key("space", reveal_hiragana)

    while True:
        if keyboard.is_pressed("esc"):
            break
        
    