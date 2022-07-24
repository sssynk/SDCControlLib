import python_library.sdc as sdc
import time

car = sdc.SDCar("192.168.1.51", "3000")
car.forward(2)
time.sleep(1)
car.setLeftMotor(-1)
car.setRightMotor(4)
time.sleep(3)
car.forward(2)
time.sleep(2)
car.brake()
