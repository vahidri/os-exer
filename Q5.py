"""
Vahid Ramazani
OS, chapter 6, exercise 5
"""

from schedulingEngine import *

if '__main__' == __name__ :
    n = int(input('process count? '))
    print('entered length')
    for i in range(n):
        e, l = input().split()
        p = process()
        p.entered = int(e)
        p.length = int(l)
        procs.append(p)
    procs_was = procs

    print('>>>RR(5)')
    init(procs_was)
    rr(5)
    showall()

