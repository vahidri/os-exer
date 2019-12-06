##semaphores
mutex = 1
ox = 0 #oxygen count
hy = 0 #hyrdogen count
flag_ox = 0 #gets true/1 after taking 2 hydrogens
flag_hy = 0 #gets true/1 after taking 1 oxygen

def prepare():
    if hy >= 2 and ox >= 1 :
        hy -= 2
        signal(flag_hy)
        ox -= 1
        signal(flag_ox)

def make_water():
    wait(flag_hy) #take the 2 hydrogens
    wait(flag_ox) #take the 1 oxygen
    print ('water molecule') #make H2O
    
def oxygen():
    wait(mutex)
    ox += 1 #new oxygen
    ##make water
    prepare()
    signal(mutex)
    make_water()

def hydrogen():
    wait(mutex)
    hy += 1
    prepare()
    signal(mutex)
    make_water()

