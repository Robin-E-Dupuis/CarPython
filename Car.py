class Car:

    def set_speed(self):
        self.speed = float(input("Enter the speed of the car: "))

    def set_model(self):
        self.model = input("Enter the model of the car: ")

    def set_supercar(self):
        self.supercar = input("Enter Yes/y if the car is a supercar or No/n if it isn't: ").lower()

    def get_speed(self):
        return self.speed

    def get_model(self):
        return self.model

    def get_supercar(self):
        if self.supercar == "yes" or self.supercar == "y":
            return True
        elif self.supercar == "no" or self.supercar == "n":
            return False
        else:
            return "Your input is incorrect"



car = Car()
car.set_speed()
car.set_model()
car.set_supercar()
print("The current speed is", car.get_speed())
print("The current model of the car is", car.get_model())
print("The current car is a supercar:", car.get_supercar())
