# This file is placed in the Public Domain.


"fleet"


from obj import values
from run import broker
from thr import name


def flt(event):
    "list of bots."
    bots = values(broker.objs)
    try:
        event.reply(bots[int(event.args[0])])
    except (IndexError, ValueError):
        event.reply(",".join([name(x).split(".")[-1] for x in bots]))
