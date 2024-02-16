


class Test:

    name="Python"
    __age=25
    def __m1(self):
        print("Inside the class and method =",self.name)
        print("Inside the class and method = ",self.__age)


t=Test()
t.m1()
print("Outside the class =" ,t.name)
#print("Outside the class =", t.__age)

