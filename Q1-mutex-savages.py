##semaphores
mutex=1
awaken_cook=0
pot_filled=0

meals_left=M #0 is valid too

def Cook():
  while True:
    wait(awaken_cook)
    meals_left=M #fills the pot
    signal(pot_filled)
  ##sleeps


def Savage():
  while True
    wait(mutex) #only one savage can eat a time
    if 0 == meals_left :
       signal(awaken_cook)
       wait(pot_filled)
    meals_left -= 1
    signal(mutex)
  ##eats

