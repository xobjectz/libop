# This file is placed in the Public Domain.
#
# pylint: disable=E0402


"fleet"


from ..object  import values
from ..run     import broker
from ..thread  import name


def flt(event):
    "list of bots."
    bots = values(broker.objs)
    try:
        event.reply(bots[int(event.args[0])])
    except (IndexError, ValueError):
        event.reply(",".join([name(x).split(".")[-1] for x in bots]))
