"""
Vahid Ramazani
OS, chapter 6, exercise 5 & 6
"""

n = 0
procs = []
errval = -1

class process():
    def __init__(self):
        self.entered = errval
        self._len = errval
        self._lenSaved = errval
        self.started = errval
        self.finished = errval

    @property
    def length(self):
        return self._len

    @length.setter
    def length(self, val):
        if self._lenSaved == errval:
            self._lenSaved = val
        self._len = val

    @property
    def turnaroundTime(self):
        return self.finished - self.entered

    @property
    def waitTime(self):
        return self.turnaroundTime - self._lenSaved

    @property
    def responseTime(self):
        return self.started - self.entered

    def isFinished(self):
        return self.finished != errval

def init(inp=None):
    global procs
    if inp is not None:
        procs = inp
    procs = sorted(procs, key= lambda item: item.entered)

def done(inp = procs):
    for p in inp:
        if not p.isFinished():
            return False
    return True

def shortest(t, inp=procs): ##find shortest
    outy = errval
    for i, p in enumerate(inp):
        if p.entered > t:
            continue
        if p.isFinished():
            continue
        if outy == errval :
            outy = i
        elif p.length < inp[outy].length:
            outy = i
    return outy

def fcfs(): ###First Come First Served
    global procs
    t = 0
    for p in procs:
        p.started = t
        t += p.length
        p.finished = t

def spn(): ##Shortest Process Next
    global procs
    t = 0
    l = [p.length for p in procs]
    while not done():
        s = shortest(t)
        p = procs[s]
        if p.started == errval:
            print(t, 'started', s+1)
            p.started = t
        t += 1
        l[s] -= 1
        if 0 == l[s]:
            p.finished = t
            print(t, 'finished', s+1)

def srt(): ##Shortest Remaining Time
    global procs
    t = 0
    while not done():
        s = shortest(t)
        p = procs[s]
        if p.started == errval:
            print(t, 'started', s+1)
            p.started = t
        t += 1
        p.length -= 1
        if 0 == p.length:
            p.finished = t
            print(t, 'finished', s+1)

def rr(quantum): ##Round Robin
    global procs
    t = 0
    while not done():
        for i, p in enumerate(procs):
            if p.entered > t:
                continue
            if p.isFinished():
                continue
            if p.started == errval:
                print(t, 'started', i+1)
                p.started = t
            if p.length < quantum:
                t += p.length
                p.length = 0
            else:
                t += quantum
                p.length -= quantum
            if 0 == p.length:
                print(t, 'finished', i+1)
                p.finished = t

def showall():
    global procs
    w_total = 0
    t_total = 0
    print('wait, turnaround, response | entered, firstRun, finished, length')
    for p in procs:
        print(p.waitTime, p.turnaroundTime, p.responseTime, '|', p.entered, p.started, p.finished, p._lenSaved, sep='\t')
        w_total += p.waitTime
        t_total += p.turnaroundTime
    print()
    print('sum:', w_total, t_total)
    #print(w_total/len(procs), t_total/len(procs) )
    print('average:', round(w_total/len(procs), 2), round(t_total/len(procs), 2) )
    print()


def printer(inp):
    print('count:', len(inp))
    for p in inp:
        print (p.entered, p.length, '|', p.started, p.finished)
    print()

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

