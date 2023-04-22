import random

def rand(random_number1 = random.randint(0, 125), random_number2 = random.randint(0, 125),
         sep = '') ->None:
    if random_number1 > random_number2:
        print(random_number1)
    else:
        print(random_number2)
    print(random_number1,random_number2,'Завершилась первая задача','Вторая задача', sep = '\n')
rand()


def rand2(random_number1 = random.randint(0, 900), random_number2 = random.randint(0, 900), a: int = 135,
         b:int = -135,
         sep = '') ->None:
    if random_number1 - random_number2 == a:
        print('Y')
        print(random_number1, random_number2, sep='\n')
    elif random_number1 - random_number2 == b:
        print('Y')
        print(random_number1, random_number2, sep='\n')
    else:
        print('N')
        print(random_number1, random_number2, 'Завершилась вторая задача','Началась третья',sep = '\n')
rand2()

def rand3(random_number1 = random.randint(1, 12),
          sep = '') ->None:
    if  random_number1 == 12 or random_number1 == 1 or random_number1 ==2:
        print('Зима','Завершилась третья','Началась четвертая',sep = '\n')

    elif random_number1 == 3 or random_number1 == 4 or random_number1 == 5:
        print('Весна','Завершилась третья','Началась четвертая',sep = '\n')

    elif random_number1 == 6 or random_number1 == 7 or random_number1 == 8:
        print('Лето','Завершилась третья','Началась четвертая',sep = '\n')
    else:
        print(random_number1, 'Осень','Завершилась третья','Началась четвертая',sep = '\n')
rand3()

def rand4(rn1 = random.randint(-9999, 9999),rn2 = random.randint(-9999, 9999),
          rn3 = random.randint(-9999, 9999),rn4 = random.randint(-9999, 9999),
          sep = '') ->None:
    if rn1 > 10 and rn2 > 10 and rn3 > 10 and rn4 > 10:
        print(rn1,rn2,rn3,rn4,'Y','Завершилась четвертая','Началась пятая',sep = '\n')
    else:
        print(rn1,rn2,rn3,rn4,'N','Завершилась четвертая','Началась пятая',sep = '\n')
rand4()

def rand5(rn1 = random.randint(-9999, 9999), rn2 = random.randint(-9999, 9999),
          rn3 = random.randint(-9999, 9999),rn4 = random.randint(-9999, 9999),
          rn5 = random.randint(-9999, 9999),
          pol: int = 0,
          otr: int = 0,
          sep = '') ->None:
    if rn1 > 0:
        pol = pol + 1
    else:
        otr = otr + 1
    if rn2 > 0:
        pol = pol + 1
    else:
        otr = otr + 1
    if rn3 > 0:
        pol = pol + 1
    else:
        otr = otr + 1
    if rn4 > 0:
        pol = pol + 1
    else:
        otr = otr + 1
    if rn5 > 0:
        pol = pol + 1
    else:
        otr = otr + 1
        print(rn1, rn2, rn3, rn4,rn5, 'Количество положительных = ', pol,'Шестая задача', sep ='\n')
rand5()

def rand6(let: int = random.randint(0, 100), mes: int = random.randint(0, 9999),
          d = 29, sep = '') ->None:
        print(let * 12 + mes * d)
rand6()