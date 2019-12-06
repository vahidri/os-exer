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

    printer(procs_was)

    print('>>>FCFS')
    init(procs_was)
    fcfs()
    showall()

    print('>>>SPN')
    init(procs_was)
    spn()
    showall()
    
    print('>>>SRT')
    init(procs_was)
    srt()
    showall()

    print('>>>RR(3)')
    init(procs_was)
    rr(3)
    showall()

