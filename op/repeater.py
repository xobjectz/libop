# This file is placed in the Public Domain.


"repeater"


from op.thread import launch
from op.timer  import Timer


class Repeater(Timer):

    "Repeater"

    def run(self):
        launch(self.start)
        super().run()


def __dir__():
    return (
        'Repeater',
    )
