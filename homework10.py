class Employee:
    def __init__(self, fname: str, lname: str, salary: float, department: str):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.department = department
        self.is_fired = False

    def get_fname(self):
        return self.fname
    
    def get_lname(self):
        return self.lname
        
    def get_salary(self):
        return "$" + "{:0.2f}".format(self.salary)
    
    def get_department(self):
        return self.department
    
    def get_is_fired(self):
        return self.is_fired
    
    def set_fname(self, fname):
        self.fname = fname

    def set_lname(self, lname):
        self.lname = lname

    def set_salary(self, salary):
        self.salary = salary

    def set_department(self, department):
        self.department = department

    def set_is_fired(self, is_fired):
        self.is_fired = is_fired

    def get_full_name(self):
        return self.fname + " " + self.lname
    
def main():
    employee_ben = Employee("Ben", "Zakielarz", 100000, "Backend Developer")
    print(employee_ben.get_fname(), employee_ben.get_lname(), employee_ben.get_salary(), employee_ben.get_department(), f"Employment status: {"Fired" if employee_ben.get_is_fired() else "Employed"}")
    employee_ben.set_salary(120000)
    print("Raise Given")
    print(employee_ben.get_full_name(), employee_ben.get_salary())
    employee_ben.is_fired = True
    print("Employee Fired")
    print(f"Employment status: {"Fired" if employee_ben.get_is_fired() else "Employed"}")
    
if __name__ == "__main__":
    main()