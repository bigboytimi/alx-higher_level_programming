#!/usr/bin/python3



def append_after(filename="", search_string="", new_string=""):
    text = ""
    with open(filename, "r") as nf:
        for line in nf:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as wf:
        wf.write(text)
