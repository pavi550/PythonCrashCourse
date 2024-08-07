def outer():
    x = 'local'    # local variable x
    print('1)x in outer',x)
    def inner():     # inner function
        nonlocal x    # referencing the x from outer function
        x = 'nonlocal'
        print('Inside inner',x)

        def inner_two():
            nonlocal x
            x = "Demo_done"
            print("X inside inner_two",x)
        inner_two()
    print('2)x in outer', x)
    inner()
    print('3)x in outer', x)
print('Outside the function ')
outer()
