import python_library.sdc as sdc
import keyboard  # using module keyboard


car = sdc.SDCar("192.168.1.51", "3000")

forward_pressed = False
backward_pressed = False
left_pressed = False
right_pressed = False
while True:  # making a loop
    if keyboard.is_pressed('w'):
        if not forward_pressed:
            forward_pressed = True
            car.forward(7)
    else:
        if forward_pressed:
            forward_pressed = False
            car.brake()
    if keyboard.is_pressed('s'):
        if not backward_pressed:
            backward_pressed = True
            car.forward(-7)
    else:
        if backward_pressed:
            backward_pressed = False
            car.brake()
    if keyboard.is_pressed('a'): 
        if not left_pressed:
            left_pressed = True
            car.setRightMotor(7)
    else:
        if left_pressed:
            left_pressed = False
            car.setRightMotor(0)
    if keyboard.is_pressed('d'): 
        if not right_pressed:
            right_pressed = True
            car.setLeftMotor(-7)
    else:
        if right_pressed:
            right_pressed = False
            car.setLeftMotor(0)
