#9. Итоги. Финальное задание
#  напишите свою функцию, которая будет справляться с угадыванием меньше чем за 20 попыток.
# исправленная версия
"Программа угадает число менее чем за 20 попыток"
import numpy as np

def random_predict(number: int = 1) -> int:
    
    min_munber = 1
    max_number = 100
    count = 0
    
    while min_munber <= max_number :
        
        predict_number = int((min_munber + max_number )/2)
        count += 1
        
        if predict_number == number:
            return count
        if predict_number > number:
            max_number  = predict_number - 1
        else:
            min_munber = predict_number + 1
    return None

def score_game(random_predict) -> int:
    
    count_ls = []
    
    random_array = np.random.randint(1, 101, size=(1000))
    
    for n in random_array:
        count_ls.append(random_predict(n))
    
    score = int(np.mean(count_ls))
    print(f"Программа угадывает число в среднем за:{score} попыток")
    return score

if __name__ =="__main__":
    score_game(random_predict)

