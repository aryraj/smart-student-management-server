class Employee:

    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total number of employees ", Employee.empCount

    def displayEmployee(self):
        print "Name: " + self.name, "Salary: ", self.salary


emp1 = Employee("Aryan", 2000)
emp2 = Employee("Rashi", 4000)

emp1.displayEmployee()
emp2.displayEmployee()

print "Total employees: ", Employee.empCount

emp1.age = 7
emp2.age = 8

print "Age of employee1: ", emp1.age