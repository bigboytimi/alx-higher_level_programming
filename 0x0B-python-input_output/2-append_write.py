#!/usr/bin/python3


def append_write(filename="", text=""):
    with open(filename, "a", encoding="utf-8") as new_file:
        new_file.append(text)

        number = new_file.tell()
        return number

