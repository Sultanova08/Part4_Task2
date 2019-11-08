# 2)Airplane
# Создайте новый класс Airplane. Создайте следующие характеристики (полей)
# объекAта:
# ● make (марка)
# ● model
# ● year
# ● max_speed
# ● odometer
# ● is_flying
# и методы имитирующих поведение самолета take off (взлет), fly (летать), land
# приземление). Метод take off должен изменить is_flying на True, а land на False. По
# умолчанию поле is_flying = False. Метод fly должен принимать расстояние полета и
# изменять показания одометра (километраж). Создайте 1 объект класса и используйте
# все методы класса.

# class Airplane():
#     def __init__ (self,make,model,year,max_speed,odometer,is_flying):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.max_speed = max_speed
#         self.odometer = odometer
#         self.is_flying = False
#         print("The info about airplane: ")
       

#     def take_off(self):
#         print("Airplane is now"  )
#         print(self.is_flying is False)
#     def fly (self):
#         print ("Airplane fly with speed " + self.max_speed)
#     def land (self):
#         print ("Then Airplane is")
#         print(self.is_flying is True)

# action_with_airplane = Airplane("SDS", "T-198", "2000", "1000km/h", "1800m", None)

# # print(action_with_airplane.make)
# # print(action_with_airplane.model)
# # print(action_with_airplane.year)
# # print(action_with_airplane.max_speed)
# # print(action_with_airplane.odometer)
# # print(action_with_airplane.is_flying)
# action_with_airplane.take_off()
# action_with_airplane.fly()
# action_with_airplane.land()

class Airplane:
    def __init__(self, make, model, year, max_speed):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self. odometer = 0
        self.is_flying = False

    def take_off(self):
        self.is_flying = True

    def land(self):
        self.is_flying = False

    def fly(self, km):
        self.odometer += km

airplane = Airplane('Boing', '737', '2000', '817')
airplane.take_off()
print(airplane.is_flying)
airplane.fly(500)
print(airplane.odometer)
airplane.land()
print(airplane.is_flying)
airplane.fly(500)
print(airplane.odometer)
