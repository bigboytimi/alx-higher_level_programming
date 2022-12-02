#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    sum = 0

    arg_num = len(sys.argv)

    for i in range(arg_num):
        if i != 0:
            num = int(sys.argv[i])
            sum += num

    print(sum)
