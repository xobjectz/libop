# This file is placed in the Public Domain.


"original programmer"


import os
import sys


path = os.path.dirname(__file__)
libpath = os.path.join(path, "lib")
runpath = os.path.join(path, "run")


sys.path.insert(0, libpath)
