
lines = int(input())
for line in range(0,lines):
    k = 1
    t = 0
    s = []
    i = input()
    minimum, letters = i.split(" ")
    print(i)
    for letter in letters:
        if letter == "S":
            t += k
            s.append(k)
        else:
            k = k << 1
            print(k)
    print(s, minimum)
        
