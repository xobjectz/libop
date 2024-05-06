# This file is placed in the Public Domain.
#
# pylint: disable=R0902,R0903,W0105,W0212,W0718


"broker"


from .object import Default, Object


rpr = object.__repr__


class Broker:

    "Broker"

    def __init__(self):
        self.objs = Object()

    def add(self, obj):
        "add an object to the broker."
        setattr(self.objs, rpr(obj), obj)

    def first(self):
        "return first object."
        for key in keys(self.objs):
            return getattr(self.objs, key)

    def get(self, orig):
        "return object by origin (repr)"
        return getattr(self.objs, orig, None)

    def remove(self, obj):
        "remove object from broker"
        delattr(self.objs, rpr(obj))

"interface"


def __dir__():
    return (
        'Broker',
    )