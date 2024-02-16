
def Outer_fun(name):

    def Inner_fun():
        return "Hello " + name

    return Inner_fun()



x=Outer_fun("Logesh")
print(x)