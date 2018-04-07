"""trouble sort"""
cases = int(input())

for thisCase in range(cases):
    count = input()
    
    MainList = input().split(" ")
    print(MainList, count, cases)
    L1 = sorted(MainList[::2])
    L2 = sorted(MainList[1::2])

    #make sure all the elements in L1 < L2

    fil = filter(lambda i:int(L1[i])>int(L2[i]), range(len(L2)))
    try:
        print("Case #",1 + thisCase,": ", next(fil)*2)
    except StopIteration:
        if L1[1]<L2[0]:
            print (1)
        print("Case #",1 + thisCase,": OK")
