# This file is placed in the Public Domain.


"list of commands"


def cmd(event):
    "list commands."
    from op.client import Command # pylint: disable=C0415
    event.reply(",".join(sorted(list(Command.cmds))))