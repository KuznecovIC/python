a = 5

def func() 
    a = 10
    print(a)

def func2() 
    a = 15
    print(a)

func()

def func3() 
    print(a)

def func4(a: int) 
    print(a)

def func6()
    global a 
    a = 20
    print(f'{a=} внутри')

print(f'{a=} вне')

func6()

func3()

func4(10)
func2()
