#1

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

class button:

    def __init__(self, textbox = None, checkbox = None,
                 radiobutton = None, webtables = None, buttons = None, links = None,
                 broken = None, uploaddownload = None, dynamicprop = None):
        self.textbox = textbox
        self.checkbox = checkbox
        self.radiobutton = radiobutton
        self.webtables = webtables
        self.buttons = buttons
        self.links = links
        self.broken = broken
        self.uploaddownload = uploaddownload
        self.dynamicprop = dynamicprop

    def click(self):
       return 'Клик по кнопке - {}'.format(self.textbox)

textbox = button('textbox', 'button#textbox')
checkbox = button('checkbox ', '1', 'button#checkbox')
radiobutton = button('radiobutton ', '1', 'button#radiobutton')

print(textbox.click())
print(checkbox.click())
print(radiobutton.click())