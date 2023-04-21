def task_1(q: int = 1,
           w: float = 2.5,
           e: str = 'строка',
           r: list = (1, 2, 3),
           t: bool = True,
           sep = ''
           ):
    print(type(q),
          type(w),
          type(e),
          type(r),
          type(t),
          sep = '\n') # блок, принадлежащий функции
# Конец функции
task_1()

#c аннотацией?
def task_12(y: int) -> None:
    print(type(y))
    # Конец функции
task_12(3)

def task_2(a: list = [1, 2, 3, 5, 8, 13, 21]) -> None:
    print(a[0:3])
    # Конец функции
task_2()

def task_3(u: int = 3) -> None:
    print(u ** 2)
    # Конец функции
task_3()
