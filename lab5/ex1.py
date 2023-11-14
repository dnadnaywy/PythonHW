import math


class Shape:
    def area(self): pass

    def perimeter(self): pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius
        self.pi = math.pi

    def area(self):
        return self.pi * self.radius ** 2

    def perimeter(self):
        return 2 * self.pi * self.radius


class Rectangle(Shape):
    def __init__(self, length, height):
        self.length = length
        self.height = height

    def area(self):
        return self.length * self.height

    def perimeter(self):
        return 2 * (self.length + self.height)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.edge1 = a
        self.edge2 = b
        self.edge3 = c

    def perimeter(self):
        return self.edge1 + self.edge2 + self.edge3

    def area(self):
        semiperimeter = self.perimeter() / 2
        return (semiperimeter * (semiperimeter - self.edge1) * (semiperimeter - self.edge2) * (
                semiperimeter - self.edge3)) ** 0.5


# --------------------------------------------------------------------ex2

class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, sum): pass


class SavingsAccount(Account):

    def __init__(self, interest_rate, account_number, balance=0):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def deposit(self, sum):
        if sum > 0:
            self.balance += sum
            print(f"Deposited amount: ${sum}. For account {self.account_number}, the new balance: ${self.balance}")
        else:
            print("No deposited amount, you have to add a number > 0.")

    def interest_calculator(self):
        interest_amount = self.balance * self.interest_rate
        print(f"The interest for your account is: ${interest_amount} at an interest rate of: ${self.interest_rate}")


class CheckingAccount(Account):

    def deposit(self, sum):
        if sum > 0:
            self.balance += sum
            print(f"Deposited amount: ${sum}. For account {self.account_number}, the new balance: ${self.balance}")
        else:
            print("No deposited amount, you have to add a number > 0.")

    def withdrawal(self, sum):
        if sum > self.balance or sum < 0:
            print("It is not possible a withdrawal, insufficient balance or the amount is below 0.")
        else:
            self.balance -= sum
            print(f"Withdrawed amount: ${sum}. For account {self.account_number}, the new balance: ${self.balance}")


# -----------------------------------------------------------------ex3
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def calculate_mileage(self): pass


class Car(Vehicle):

    def __init__(self, make, model, year, distance, fuel_consumed, tow_capacity):
        super().__init__(make, model, year)
        self.distance = distance
        self.fuel_consumed = fuel_consumed
        self.tow_capacity = tow_capacity

    def calculate_mileage(self):
        mileage = self.distance / self.fuel_consumed
        print(f"The mileage for this car is {mileage} miles/gallon")

    def calculate_tow_capacity(self):
        print(f"Your tow capacity is {self.tow_capacity} pounds")


class Truck(Vehicle):

    def __init__(self, make, model, year, distance, fuel_consumed, tow_capacity):
        super().__init__(make, model, year)
        self.distance = distance
        self.fuel_consumed = fuel_consumed
        self.tow_capacity = tow_capacity

    def calculate_mileage(self):
        mileage = self.distance / self.fuel_consumed
        print(f"The mileage for this truck is {mileage} miles/gallon")

    def calculate_tow_capacity(self):
        print(f"Your tow capacity is {self.tow_capacity} pounds")


class Motorcycle(Vehicle):

    def __init__(self, make, model, year, distance, fuel_consumed):
        super().__init__(make, model, year)
        self.distance = distance
        self.fuel_consumed = fuel_consumed

    def calculate_mileage(self):
        mileage = self.distance / self.fuel_consumed
        print(f"The mileage for this motorcycle is {mileage} miles/gallon")


# ---------------------------------------------------------------------ex4

class Employee:
    salary = 0
    role = ""

    def set_salary(self, salary):
        self.salary = salary

    def set_role(self, role):
        self.role = role

    def get_salary(self):
        return self.salary

    def get_role(self):
        return self.role

    def print_info_about_employee(self):
        print(f"The employee has {self.role} as role and a salary of {self.salary}")


class Manager(Employee):
    def __init__(self):
        self.salary = 9000
        self.role = "Manager"

    def set_employees_role(self, employee: Employee, role):
        employee.set_role(role)

    def set_employees_salary(self, employee: Employee, salary):
        employee.set_role(salary)


class Engineer(Employee):

    def set_written_code(self, code):
        self.code = code

    def get_written_code(self):
        print(f"The engineer uploaded the following code:\n{self.code}")
        return self.code


class Salesperson(Employee):

    def set_sale(self, units, price_of_unit):
        self.units = units
        self.money_made = units * price_of_unit

    def get_sale(self):
        print(f"The salesperson sold {self.units} units and brought ${self.money_made} ")
        return self.units, self.money_made


# --------------------------------------------------------------------ex5

class Animal:
    def eat(self): pass

    def set_type(self, type):
        self.type = type

    def set_name(self, name):
        self.name = name

    def reproduction(self): pass


class Mammal(Animal):
    def __init__(self, name):
        self.set_name(name)
        self.set_type("Mammal")
        self.eating()
        self.reproducting()

    def eating(self):
        self.eat = "omnivore"

    def reproducting(self):
        self.reproduction = "pui vii"

    def print_info_about_animal(self):
        print(f"The name of this {self.type} is {self.name}, it is {self.eat}")


class Bird(Animal):
    def __init__(self, name):
        self.set_name(name)
        self.set_type("Bird")
        self.eating()
        self.reproducting()

    def eating(self):
        self.eat = "herbivore"

    def reproducting(self):
        self.reproduction = "eggs"

    def print_info_about_animal(self):
        print(f"The name of this {self.type} is {self.name}, it is {self.eat}")


class Fish(Animal):
    def __init__(self, name):
        self.set_name(name)
        self.set_type("Fish")
        self.eating()
        self.reproducting()

    def eating(self):
        self.eat = "carnivore"

    def reproducting(self):
        self.reproduction = "eggs"

    def print_info_about_animal(self):
        print(f"The name of this {self.type} is {self.name}, it is {self.eat}")


# --------------------------------------------------------------------ex6

class LibraryItem:
    def __init__(self, title, item_id, num_copies):
        self.title = title
        self.item_id = item_id
        self.num_copies = num_copies
        self.checked_out_copies = 0

    def print_info(self):
        print(f"Title: {self.title}")
        print(f"Item ID: {self.item_id}")
        print(f"Available Copies: {self.num_copies - self.checked_out_copies}")

    def checkout(self):
        if self.checked_out_copies < self.num_copies:
            self.checked_out_copies += 1
            print("Item checked out successfully.")
        else:
            print("All copies are currently checked out.")

    def return_item(self):
        if self.checked_out_copies > 0:
            self.checked_out_copies -= 1
            print("Item returned successfully.")
        else:
            print("No copies are currently checked out.")


class Book(LibraryItem):
    def __init__(self, title, item_id, num_copies, author):
        super().__init__(title, item_id, num_copies)
        self.author = author

    def print_info(self):
        super().print_info()
        print(f"Author: {self.author}")


class DVD(LibraryItem):
    def __init__(self, title, item_id, num_copies, director):
        super().__init__(title, item_id, num_copies)
        self.director = director

    def print_info(self):
        super().print_info()
        print(f"Director: {self.director}")


class Magazine(LibraryItem):
    def __init__(self, title, item_id, num_copies, publication_frequency):
        super().__init__(title, item_id, num_copies)
        self.publication_frequency = publication_frequency

    def print_info(self):
        super().print_info()
        print(f"Publication frequency: {self.publication_frequency}")


if __name__ == "__main__":
    # ------------------------------------------------------------ex1
    # triangle = Triangle(3, 4, 5)
    # print("Area of a triangle: " + str(triangle.area()) + ". Perimeter: " + str(triangle.perimeter()))
    #
    # circle = Circle(3)
    # print("Perimeter of a circle: " + str(circle.perimeter()) + ". Area of a circle: " + str(circle.area()))
    #
    # rectangle = Rectangle(3, 4)
    # print("Perimeter of a rectangle: " + str(rectangle.perimeter()) + ". Area of a rectangle: " + str(rectangle.area()))

    # ------------------------------------------------------------ex2
    # savings_account = SavingsAccount(0.02, 123, 100)
    # savings_account.deposit(200)
    # savings_account.interest_calculator()
    #
    # print()
    #
    # checking_account = CheckingAccount(124, 100)
    # checking_account.deposit(100)
    # checking_account.withdrawal(200)

    # ------------------------------------------------------------ex3
    # car = Car("Toyota", "Camry", 2022, 200, 100, 150)
    # truck = Truck("Ford", "F-150", 2020, 500, 100, 300)
    # motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2021, 200, 80)
    # car.calculate_mileage()
    # truck.calculate_mileage()
    # motorcycle.calculate_mileage()
    # car.calculate_tow_capacity()

    # ----------------------------------------------------------------ex4
    # manager = Manager()
    # manager.print_info_about_employee()
    # engineer = Engineer()
    # manager.set_employees_role(engineer, "Engineer")
    # manager.set_employees_salary(engineer, 14000)
    # engineer.print_info_about_employee()

    # ------------------------------------------------------------------ex5
    # fish = Fish("piranha")
    # fish.print_info_about_animal()
    # cat = Mammal("cat")
    # cat.print_info_about_animal()
    # bird = Bird("pigeon")
    # bird.print_info_about_animal()

    # -----------------------------------------------------------------ex6
    book = Book("Un cal intr-o mare de lebede", 1, 2, "Raluca Nagy")
    book.print_info()