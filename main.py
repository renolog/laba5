def r1():
    sp = int(input('Введите число: '))
    a = [1, 2, 3, 4, 6]
    if sp in a:
        print(a, '\n ','Поздравляю, Вы угадали число!')
    else:
        print(a, '\n ','Нет такого числа!')

def r2():
        lis2 = [1, 2, 4, 6, 7, 3, 5, 8, 4]
        pov = {str (x) for x in lis2 if lis2.count(x) > 1 }
        x = lambda: print('Ничего')
        y = lambda: print(' '.join(pov))
        x() if len(pov) < 1 else y()
def r3():
    week = ('ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ', 'ВС')
    weekends = int(input())
    print('Выходной:', week[:-weekends-1:-1])
    print('Рабочий день:', week[:-weekends])

def r4():
    fam1 = ['иванов', 'сидоров', 'петров']
    fam2 = ['кузнецов', 'грачев', 'скворцов']
    foot = (fam1[0], fam2[1], fam2[2])
    print(*fam1)
    print(*fam2)
    print(*foot)
    print(len(foot))
    foot = tuple(sorted(foot))
    print(foot)
    if 'иванов' in foot:
        print("иванов есть в команде")

r2()