import numpy as np

def game_core_v4():
    count = 0
    number = np.random.randint(1, 100)
    newlist = []
    for i in range(1,101):
        newlist.append(i)
        
    low = 1 #newlist[0]
    high = 100 #newlist[100]
    mid = (low + high) // 2
    while low <= high:
        count += 1
        if number < newlist[mid]:
           high = mid
        elif number > newlist[mid]:
            low = mid
        else:
            break
    return count
    