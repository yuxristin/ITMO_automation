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
        print('Зима')

    elif random_number1 == 3 or random_number1 == 4 or random_number1 == 5
        print('Весна')

    elif random_number1 == 6 or random_number1 == 7 or random_number1 == 8
        print('Лето')
    else:
        print(random_number1, 'Осень','Началась четвертая',sep = '\n')
rand2()