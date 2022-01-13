class Car:
    def __init__(self, color, typ, year):
        self.color = color
        self.typ = typ
        self.year = year

    @staticmethod
    def on():
        print('Автомобиль заведен')

    @staticmethod
    def off():
        print('Автомобиль заглушен')

    def YCar(self):
        ycar = self.year
        print(ycar)

    def TCar(self):
        tcar = self.typ
        print(tcar)

    def Ccar(self):
        cCar = self.color
        print(cCar)


ob = Car('красный', 'дизель', '1995')
ob.on()
ob.off()
ob.YCar()
ob.TCar()
ob.Ccar()