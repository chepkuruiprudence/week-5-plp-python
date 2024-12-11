class Animal:
  def move(self):
    pass

class Bird(Animal):
  def move(self):
      print("Flying") 

class Dog(Animal):
    def move(self):
        print("Walking")

class Fish(Animal):
    def move(self):
        print("Swimming")

class vehicle:
   def move(self):
      pass

class Car(vehicle):
    def move(self):
        print("drive")

class Plane(vehicle):
    def move(self):
        print("Flying")

class Boat(vehicle):
    def move(self):
        print("Swimming")

#class instances
bird = Bird()
dog = Dog()
fish = Fish()
car = Car()
plane = Plane()
boat = Boat()

#calling
dog.move() 
bird.move() 
fish.move() 
car.move() 
plane.move() 
boat.move()
