# Usnig init method and self keyword in python
class Car:
        def __init__(self, speed, color):
                print(speed)
                print(color)
                print('the __init__is called')

ford = Car(200,'red')
honda = Car(250,'blue')
audi = Car(300,'black')