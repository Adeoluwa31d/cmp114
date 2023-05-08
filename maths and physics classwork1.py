class Math:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2

    def power(self, num1 , num2):
        return num1 ** num2

class Physics:

    def speed(self, distance, time):
        return distance / time

    def acceleration(self, velocity, time):
        return velocity / time

    def force(self, mass, acceleration):
        return mass * acceleration

    def energy(self, mass, velocity):
        return 0.5 * mass * velocity ** 2

    def momentum(self, mass, velocity):
        return mass * velocity


# Prompt the user to select which class to use
while True:
    user_choice = input("Enter 'math' or 'physics': ")
    if user_choice.lower() == "math" or user_choice.lower() == "physics":
        break
    print("Invalid choice, please try again.")

# Prompt the user to select which operation to perform
if user_choice.lower() == "math":
    calculator = Math()
    print("Choose an operation: add, subtract, multiply, divide, power")
    operation = input("Enter operation: ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == "add":
        print(calculator.add(num1, num2))
    elif operation == "subtract":
        print(calculator.subtract(num1, num2))
    elif operation == "multiply":
        print(calculator.multiply(num1, num2))
    elif operation == "divide":
        print(calculator.divide(num1, num2))
    elif operation == "power":
        print(calculator.power(num1, num2))
else:
    calculator = Physics()
    print("Choose an operation: speed, acceleration, force, energy, momentum")
    operation = input("Enter operation: ")
    if operation == "speed":
        distance = float(input("Enter distance: "))
        time = float(input("Enter time: "))
        print(calculator.speed(distance, time))
    elif operation == "acceleration":
        velocity = float(input("Enter velocity: "))
        time = float(input("Enter time: "))
        print(calculator.acceleration(velocity, time))
    elif operation == "force":
        mass = float(input("Enter mass: "))
        acceleration = float(input("Enter acceleration: "))
        print(calculator.force(mass, acceleration))
    elif operation == "energy":
        mass = float(input("Enter mass: "))
        velocity = float(input("Enter velocity: "))
        print(calculator.energy(mass, velocity))
    elif operation == "momentum":
        mass = float(input("Enter mass: "))
        velocity = float(input("Enter velocity: "))
        print(calculator.momentum(mass, velocity))
