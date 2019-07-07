def simple_generator():
    yield 1
    yield 2
    yield 3


if __name__  == '__main__':
    gen = simple_generator()
    print(gen)
    print(next(gen))
    print(next(gen))
    print(next(gen))

