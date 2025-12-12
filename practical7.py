class Employee:
    def __init__(self, emp_name, emp_age, emp_service_year, emp_salary):
        self._name = emp_name
        self._age = emp_age
        self._service_year = emp_service_year
        self._salary = emp_salary
        print(f"Constructor called for {self._name}")

    def __del__(self):
        # Python's garbage collection is automatic. 
        # The __del__ method is not guaranteed to be called at exit like C++ destructors, 
        # but is used here to mirror the C++ behavior when the object is destroyed.
        print(f"Destructor called for {self._name}")

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def service_year(self):
        return self._service_year

    @property
    def salary(self):
        return self._salary

    def display_details(self):
        print("\n--- Employee Details ---")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Service Years: {self.service_year}")
        print(f"Salary: ${self.salary:,.2f}")

if __name__ == "__main__":
    print("Creating an employee object...")
    emp1 = Employee("Alice Johnson", 45, 20, 95000.00)

    print("\nAccessing data via properties:")
    print(f"Employee Name: {emp1.name}")
    print(f"Employee Age: {emp1.age}")
    print(f"Employee Salary: ${emp1.salary:,.2f}")
    
    emp1.display_details()

    print("\nProgram finished. emp1 is about to go out of scope.")
    # The __del__ method will be triggered by Python's garbage collector, typically right after this print statement finishes.
