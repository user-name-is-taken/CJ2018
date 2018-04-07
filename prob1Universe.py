import re

lines = int(input())
for line in range(0,lines):
    charges = 0
    cur_shot = 1
    damage = 0
    shots = []
    i = input()
    minimum, letters = i.split(" ")
    minimum = int(minimum)
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
    """
problem: swaping one position is a swap, you can't swap multiple
indexes in one swap

1 swap: divide the first occurance of the largest index by 2
subtract from damage
    """
    print(shots)
    swaps = 0
    while len(shots)>0 and (damage > minimum) and (shots[-1] > 1):
        damage -= (shots[-1]//2)
        shots[-1]/=2
        swaps += 1
        shots = sorted(shots)
    if(damage > minimum):
        print("case #",line+1,": IMPOSSIBLE")
    else:
        print("Case #",line+1,": ",swaps)
        
