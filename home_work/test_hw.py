def test1():
   assert ('home', 'work') == ('home', 'work')


def test2():
   assert not 'QA' == 'QC'


def test3():
   assert not (1, 1, 2, 3, 5) == (2, 3, 5)



print("test1,test2,test3")
