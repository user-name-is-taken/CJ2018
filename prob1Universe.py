import re

lines = int(input())
for line in range(0,lines):
    charges = 0
    cur_shot = 1
    damage = 0
    shots = []
    i = input()
    minimum, letters = i.split(" ")
    print(i)
    lastStart = -1
    for letter in re.finditer("C",letters):
        thisStart = letter.start()
        deltaShots = (thisStart - lastStart - 1)#charges in a row?
        damage += cur_shot * deltaShots
        shots += ([cur_shot,] * deltaShots)
        cur_shot = cur_shot << 1
        charges += 1
        lastStart = thisStart
    #add for shots at the end of the line here
    thisStart = len(letters)
    deltaShots = (thisStart - lastStart - 1)#charges in a row?
    damage += cur_shot * deltaShots
    shots += ([cur_shot,] * deltaShots)
    lastStart = thisStart

    #performs swaps
    print(shots)
    swaps = 0
    while (damage > minimum) and (shots[-1] > 1):
        damage -= (shots[-1]-1)
        del(shots[-1])
        swaps += 1
    
    
        
