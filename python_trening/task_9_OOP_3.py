class Soda:
    def __init__(self, dobavka = None):
        self.dobavka = dobavka

    def show(self):
        if self.dobavka:
            print('С добавкой')
        else:
            print('без добавки')

drink1 = Soda()
drink2 = Soda('X')
drink1.show()
drink2.show()

