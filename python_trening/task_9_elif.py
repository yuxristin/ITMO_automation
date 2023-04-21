num_float = 3.4

#Varianty
# num_float = 0
# num_foat = -4.5



def pozit(num_float: int = 3) -> None:
    if num_float > 0:
        print('Pozitive')
    elif num_float == 0:
        print('Null')
    else:
        print ('Minus')
pozit()

def permit(permit_print: bool = True, num: int = 3) -> None:
    if num > 0 and permit_print:
        print(' положить')
    elif not permit_print:
        print('Печать запрещена')
permit()


def chislo(c: int = 150) -> None:
    if c > 100 or c < -100:
        print('AWD')
    else:
        print('2WD')
chislo()