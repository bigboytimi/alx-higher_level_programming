#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4

    arr = dir(hidden_4)

    for i in arr:
        if i[:2] != "__":
            print(i)

