# This file is placed in the Public Domain.
#
# pylint: disable=C0415


"list of commands"


def cmd(event):
    "list commands."
    from op.handler import Command
    event.reply(",".join(sorted(list(Command.cmds))))
