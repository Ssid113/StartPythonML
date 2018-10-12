#!/usr/bin/env python3
from sys import argv
from pathlib import Path
from filecmp import cmp

d={}

def add(p):
    global d
    if p.is_file():
        size=p.stat().st_size
        if size in d:
            d[size].append(p)
        else:
            d[size]=[p]
    elif p.is_dir():
        for x in p.iterdir():
            add(x)

for x in argv[1:]:
    p=Path(x)
    if p.exists():
        add(p.absolute())
    else:
        print(f'{x} does not exist')

for s in reversed(sorted(d.keys())):
    if len(d[s])>1:
        l=[]
        for x in sorted(d[s]):
            new=True
            for y in l:
                if cmp(str(x),str(y[0]),shallow=False):
                    y.append(str(x))
                    new=False
                    break
            if new:
                l.append([str(x)])
        for y in l:
            if len(y)>1:
                print(y)
