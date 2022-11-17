#!/usr/bin/python
import notify2
import random
from pathlib import Path
import os

os.environ['DBUS_SESSION_BUS_ADDRESS'] = 'unix:path=/run/user/1000/bus'

def get_file_content(path, split_lines=False):
    with open(path, mode='r') as f:
        if split_lines:
            return f.read().split("\n")
        else:
            return f.read()


notify2.init('Random aphorism')

def notify(message):
    notify2.Notification(message).show()
    
def random_aphorism(path=Path().home() / "Datasets/aphorisms.txt"):
    aphorisms = get_file_content(path, split_lines=True)
    aphorism = aphorisms[random.randint(0,len(aphorisms)-1)].strip()
    text, author = aphorism.split(" -- ")
    return text, author

def get_note(path=Path().home() / "Tests/note.txt"):
    note = get_file_content(path, split_lines=False)
    with open(path, "w") as f:
        f.write("")
    return note


if __name__=="__main__":
    aphorism, author = random_aphorism()
    note = get_note()
    notify(aphorism + "\n\n" + author)
    if note:
        notify(note)
    print("Aphorism", aphorism)
    print("Note", note)
