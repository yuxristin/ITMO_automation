class A:
    def __init__(self):
        self.x =10

class B(A):
    def __init__(self):
        super().__init__()
        self.y = self.x + 2

print(B().y)

b = B()
print(b.y)



textbox = button('textbox'),
textbox2 = button('checkbox'),
textbox3 = button('radio-button'),
textbox4 = button('webtables'),
textbox5 = button('links'),
textbox6 = button('broken'),
textbox7 = button('upload-download'),
textbox8 = button('upload-download'),
textbox8 = button('dynamic-properties')
