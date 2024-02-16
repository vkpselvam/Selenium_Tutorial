class Test:


    def __m1(self):

        print("private method")

    def m2(self):
        self.__m1()

t=Test()
t.m2()