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
