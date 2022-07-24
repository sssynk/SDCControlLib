import python_library.sdc as sdc
import time

car = sdc.SDCar("192.168.1.51", "3000")
print("Car Move Forward Success: "+str(car.forward(7)))
print("Sleeping")
time.sleep(2)
print("Car Move Backward Success: "+str(car.forward(-7)))
print("Sleeping")
time.sleep(2)
print("Car Brake Success: "+str(car.brake()))
