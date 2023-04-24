class Page:
    def __init__(self, url):
        self.url = url
    def get(self):
        return self.url
get1 = Page('ya.ru')

print(get1.get())