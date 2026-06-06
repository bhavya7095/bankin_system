class Vehicle:     #parent class
    def __init__(self, name, brand, price): # method1
        self.name = name
        self.brand = brand
        self.price = price
    def display(self):  # method2
        print("Name :", self.name)
        print("Brand:", self.brand)
        print("Price:", self.price)
        
class Car(Vehicle):
    def display_car(self):
        print("\n--- Car Details ---")
        self.display()

class Bike(Vehicle):
    def display_bike(self):
        print("\n--- Bike Details ---")
        self.display()

class SportsCar(Car):
    def display_sportscar(self):
        print("\n--- Sports Car Details ---")
        self.display()

car = None
bike = None
sportscar = None
while True:
    print("\n===== Vehicle Management System =====")
    print("1. Add Vehicle")
    print("2. Show Car Details")
    print("3. Show Bike Details")
    print("4. Show SportsCar Details")
    print("5. Exit")

    choice = int(input("Enter choice: "))
    if choice == 1:
        print("\nEnter Car Details")
        cname = input("Name: ")
        cbrand = input("Brand: ")
        cprice = float(input("Price: "))
        car = Car(cname, cbrand, cprice)

        print("\nEnter Bike Details")
        bname = input("Name: ")
        bbrand = input("Brand: ")
        bprice = float(input("Price: "))
        bike = Bike(bname, bbrand, bprice)

        print("\nEnter SportsCar Details")
        sname = input("Name: ")
        sbrand = input("Brand: ")
        sprice = float(input("Price: "))
        sportscar = SportsCar(sname, sbrand, sprice)

        print("\nVehicles Added Successfully!")

    elif choice == 2:
        if car:
            car.display_car()
        else:
            print("No Car Data Available!")

    elif choice == 3:
        if bike:
            bike.display_bike()
        else:
            print("No Bike Data Available!")

    elif choice == 4:
        if sportscar:
            sportscar.display_sportscar()
        else:
            print("No SportsCar Data Available!")

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid Choice!")