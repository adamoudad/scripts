#!/bin/python
# Undo last mv commands

from pathlib import Path
history_path= Path.home() / ".zsh_history"

def filter_history(cmd="mv"):
    """
    Filter history to lines with cmd
    """
    commands = []
    with open(history_path, "r") as f:
        count = 50
        for l in f:
            command = ";".join(l.strip().split(";")[1:])
            commands.append(command)
            count -= 1
            if not count:
                break
    commands = [ c for c in commands if c.split()[0] == cmd]
    return commands

def reverse_command(command):
    """
    Return sources and destinations needed to do the inverse of command
    """
    command = command.split()
    destination = Path(command[-1])
    original_sources = [ Path(f) for f in command[1:-1] ]
    if destination.is_file():
        sources = [ destination.parent / f.name for f in original_sources ]
    else:
        sources = [ destination / f.name for f in original_sources ]
    return sources, original_sources

    
commands = filter_history("mv")
if not commands:
    exit("No command available.")

for i, c in enumerate(commands):
    print("[{}]".format(i), c)

choice = input("Your choice: ")
command = commands[int(choice)]

sources, destinations = reverse_command(command)

print("Command to undo:", command)
import shutil
for source, destination in zip(sources, destinations):
    print(str(source) + " -> " + str(destination))
    choice = input("OK?[y/N] ")
    if choice == "y":
        if destination.is_file():
            choice = input("Destination file exists. Overwrite?[y/N] ")
        if choice == "y":
            print(shutil.move(source, destination))
print("Done.")

