a= [5,10,15,29,25,30,35,40]


#a[2] = 15
print('a[2]=',a[2])


#a[0:3] = [5.10.15]
print('a[0:5] =', a[0:3])


#Изменение элемента
b = [11,12,13]
b[2] =4
print(b)


test_list = ['один','два','три','четыре','пять']

for elem  in test_list: #цикл по списку
    print(elem)


print(len(test_list)) # длина списка


test_list.append('шесть') # добавка
print(test_list)