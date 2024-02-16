class Employee:


    def __init__(self, empid, empname, salary=0):
        self.empid=empid
        self.empname=empname
        self.__salary=salary


    def getEmpdetails(self):
        print("Empid = ", self.empid)
        print("Empname = ",self.empname)



    def setSalary(self, salary):
        self.__salary=salary

    def getSalary(self):
        print("Empsalary = ",self.__salary)

e1=Employee(1,"Ravi")
e1.getEmpdetails()
e1.setSalary(30000)
e1.getSalary()

e2=Employee(2,"Logesh")
e2.getEmpdetails()
e2.setSalary(45000)
e2.getSalary()