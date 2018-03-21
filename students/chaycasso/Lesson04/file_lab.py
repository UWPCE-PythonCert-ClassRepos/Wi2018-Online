#!/usr/bin/env python3
#
import pathlib
pth = pathlib.Path("./")
for f in pth.iterdir():
    print(f.absolute())
