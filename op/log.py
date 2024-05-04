# This file is placed in the Public Domain.
#
# pylint: disable=R0903,W0105,E1102


"logging"


from .thread import Errors, tostr


class Logging:

    "Debug"

    filter = []
    out = None


def debug(txt):
    "print to console."
    for skp in Logging.filter:
        if skp in txt:
            return
    out(txt)


def enablelog(func):
    "set output function."
    Logging.out = func


def errors():
    "show exceptions"
    for exc in Errors.errors:
        out(exc)


def out(exc):
    "check if output function is set."
    txt = str(tostr(exc))
    if Logging.out:
        Logging.out(txt)


"interface"


def __dir__():
    return (
        'debug',
        'enable',
        'errors',
        'out'
    )
