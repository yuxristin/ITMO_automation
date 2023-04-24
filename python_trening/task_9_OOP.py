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