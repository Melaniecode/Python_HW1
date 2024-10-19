class Employee:
    payRate = [1, 1.2, 1.5]

    def __init__(self, base):
        self.baseSalary = base

    def salary(self, hr, bonus):
        return int(self.baseSalary * hr * Employee.payRate[bonus])

    def set_payRate(self, new_payRate):
        Employee.payRate = new_payRate

    def estimate(self, baseSalary, hr, rate):
        return int(baseSalary * hr * rate)


tom = Employee(160)
print(tom.salary(10, 1))

tom.set_payRate([1, 1.3, 1.5])
print(tom.salary(10, 1))

print(tom.estimate(160, 10, 1.25))
