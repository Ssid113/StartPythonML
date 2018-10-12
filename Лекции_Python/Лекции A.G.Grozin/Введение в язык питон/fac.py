#!/usr/bin/env python3
'В этом модуле определена функция fac'

def fac(n):
    'calculate factorial of n'
    assert type(n) is int and n >= 0
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

if __name__ == '__main__':
    from sys import argv, exit
    if len(argv) != 2:
        print('usage: ./fac.py n')
        exit(1)
    print(fac(int(argv[1])))
