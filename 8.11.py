import numpy as np
def game_core_v3(number: int = 1) -> int:
    count = 0
    low = 1
    high = 100
    
    while low <= high:
        count += 1
        mid = (low + high) // 2
        
        if mid == number:
            return count
        elif mid < number:
            low = mid + 1
        else:
            high = mid - 1
    
    return count

def score_game(random_predict) -> int:
    np.random.seed(1)
    random_array = np.random.randint(1, 100, size=1000)
    count_ls = [random_predict(number) for number in random_array]
    score = int(np.mean(count_ls))
    
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score

if __name__ == '__main__':
    score_game(game_core_v3)