#!/usr/bin/python
import notify2
import random
from pathlib import Path
import os

os.environ['DBUS_SESSION_BUS_ADDRESS'] = 'unix:path=/run/user/1000/bus'

def get_aphorisms(path):
    with open(path, mode='r') as f:
        return f.readlines()


notify2.init('Random aphorism')

def notify(message):
    notify2.Notification(message).show()
    
def random_aphorism(path):
    aphorisms = get_aphorisms(path)
    return aphorisms[random.randint(1,len(aphorisms)-1)].strip()

if __name__=="__main__":
    path = Path().home() / "Datasets/aphorisms.txt"
    aphorism = random_aphorism(path)
    notify(aphorism)
