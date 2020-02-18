import numpy as np

def game_core_v3(number):

    count = 0
    # number - загаданное число
    # predict - НЕ загаданное число, а то, которое называет кто-то в попытке отгдать загаданное число
    predict = np.random.randint(1, 100) # рандомный ответот 1 до 100

    newlist = []
    for i in range(1, 101):
        newlist.append(i)
    low = 0
    high = 100

    while number != predict:
        count += 1    
        mid = (low + high) // 2
        if number > predict:
            low = mid
        elif number < predict:
            high = mid
        else:
            break
        return count
        print(count)

game_core_v3(5)