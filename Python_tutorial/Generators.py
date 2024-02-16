
def Sample():

    yield 1
    yield "Python"
    print("Hello")
    yield 2

x=Sample()

print(next(x))
print(next(x))
print(next(x))