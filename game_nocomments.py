import numpy as np

def game_core_v4(number):
    count = 0
    predict = np.random.randint(1,100)
    low = 0
    high = 101
    
    while number != predict:
        count+=1
        predict = (low + high) // 2
        if number > predict:
            low = predict
        elif number < predict:
            high = predict
    return(count)
    
def score_game(game_core_v4):
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v4(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

score_game(game_core_v4)