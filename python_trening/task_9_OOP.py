class Button:

    def __init__(self,text, link):
        self.text = text
        self.link = link

home = Button('DOmoi','/home')
catalog_msk = Button('Каталог', '/msk/catalog')

# получаем доступ к атрибутам
print(home.text)
print('Кнопка' + home.text + 'имеет ссылку' + home.link)

print('\n')

print(catalog_msk.text)
print('Кнопка' + catalog_msk.text + 'имеет ссылку' + catalog_msk.link)


class ButtonTwo:

    def __init__(self,text, link, loc):
        self.text = text
        self.link = link
        self.loc = loc

    def click(self):
        return ' Клик по куаталогу - {}'.format(self.loc)

# Создаём экземпляры класса
home_two = ButtonTwo('ДОмой','/home','button#home')

#вызов
print(home_two.click())