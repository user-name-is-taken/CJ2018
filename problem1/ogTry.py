import re

lines = int(input())
for line in range(lines):
    #print("hi")
    cur_shot = 1
    damage = 0
    shots = []
    i = input()
    minimum, letters = i.split(" ")
    minimum = int(minimum)
    #print(i)
    lastStart = -1
    for letter in letters:
        if letter == "S":
            damage += cur_shot
            shots.append(cur_shot)
        else:
            cur_shot = cur_shot << 1

    #print(damage, " ", letters, " ", shots," ",cur_shot)
    

    
    #performs swaps
    """
problem: swaping one position is a swap, you can't swap multiple
indexes in one swap

1 swap: divide the first occurance of the largest index by 2
subtract from damage
    """
    #print(shots)
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
        
