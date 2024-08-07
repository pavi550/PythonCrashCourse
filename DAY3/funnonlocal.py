# Non-local keyword example

def outer():
    x = 'local'
    print('1)x in outer',x)
    def inner():
        nonlocal x
        x = 'nonlocal'
        print('Inside inner',x)

    print('2)x in outer', x)
    inner()
    print('3)x in outer', x)
print('Outside the function ')
outer()
