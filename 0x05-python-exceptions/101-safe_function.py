#!/usr/bin/python3


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as exerr:
        print("Exception: {}".format(exerr))
        return None
