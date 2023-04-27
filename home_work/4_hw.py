#1
from typing import Tuple


class Rectangle:
    # Это класс Rectangle

    # Объект
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    # расчет площади.
    def getArea(self):
        return self.width * self.height

    # расчёт периметра
    def getPerimeter(self):
        return self.width * 2 + self.height * 2

r1 = Rectangle(10, 5)
r2 = Rectangle(30, 3)
r3 = Rectangle(50, 2)

print("r1.длина = ", r1.width)
print("r1.ширина = ", r1.height)
print("r1.площадъ() = ", r1.getArea())
print("r1.периметр() = ", r1.getPerimeter())
print("-----------------")
print("r2.длина = ", r2.width)
print("r2.ширина = ", r2.height)
print("r2.площадь() = ", r2.getArea())
print("r2.периметр() = ", r2.getPerimeter())
print("-----------------")
print("r3.длина = ", r3.width)
print("r3.ширина = ", r3.height)
print("r3.площадь() = ", r3.getArea())
print("r3.периметр() = ", r3.getPerimeter())

#2

class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def a(self):
        return self.a

    def b(self):
        return self.b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def subtraction(self):
        return self.a - self.b
Znach = Math(5, 5)
print ('#2')
print('Sloschenie =', Znach.addition())
print('Umnoshenie =', Znach.multiplication())
print('Deleniye =', Znach.division())
print('Vichitanie =', Znach.subtraction())

#3
class Button:         #Название класса всегда с большой буквы!!

    #type = 'Кнопка'

    def __init__(self, text, loc='', type='Кнопка' ):
        self.text = text
        self.loc = loc
        self.type = type

    def click(self):
       return f'Клик по кнопке {self.text}'

buttons = ['Text Box', 'Check Box', 'Radio Button', 'Web Tables', 'Buttons', 'Links', 'Broken Links - images', 'Upload and Download', 'Dinamic Properties']

for elem in buttons:
  button = Button(elem)     # создание экземпляра класса
  print(button.click())     # вызываем метод click


class car:
    def __init__(self, year, color, type):
        self.year = year
        self.color = color
        self.type = type

        car1 = car('2000', r10, 'golf')

        def type_new(self, t_new):
            self.type = t_new

a = car('2001', 'C13', 'SEDAN')
a.type_new('334')
    print()