class Employee:
    def __init__(self,name,salery):
        self.name=name
        self.salery=salery
    def get_details(self):
        return f"نام: {self.name}  , حقوق:{self.salery} "
class Manager(Employee):
    def __init__(self,name,salery,department):
        super().__init__(name,salery)
        self.department=department
    def get_details(self):
        return f"{super().get_details()},بخش:{self.department}  "
class Intern(Employee):
    def __init__(self,name):
        super().__init__(name,2000)
class seniorEmployee(Employee):
    def __init__(self,name,base_salary):
        bonus=base_salary * 0.2
        super().__init__(name,base_salary+bonus)
        self.base_salary=base_salary
    def get_details(self):
        return f"نام:{self.name} , حقوق:{self.salery}"
        

my_employee1=Employee("علي","5000")
print(my_employee1.get_details())
my_employee2=Manager("مريم","8000","فناوري اطلاعات")
print(my_employee2.get_details())
my_employee3=Intern("رضا")
print(my_employee3.get_details())
my_employee4=seniorEmployee("نويد",20000)
print(my_employee4.get_details())
