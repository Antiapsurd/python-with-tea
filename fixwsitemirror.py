#!/usr/bin/python

import os

for d, _, fns in os.walk("."):
    for fn in fns:
        full = d + "/" + fn
        print full
        if "?" in full:
            fullok = full.split("?")[0]
            print fullok
            if not os.path.exists(fullok):
                os.rename(full, fullok)
