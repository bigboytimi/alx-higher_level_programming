#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    arg_num = len(sys.argv) - 1

    if arg_num == 0:
        print("{} arguments.".format(arg_num))
    elif arg_num == 1:
        print("{} argument:".format(arg_num))
        print("{}: {}".format(arg_num, sys.argv[1]))
    else:

        print("{} arguments:".format(arg_num))

        for i in range(arg_num + 1):
            if i != 0:
                print("{}: {}".format(i, sys.argv[i]))
