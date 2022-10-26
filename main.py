import numpy as np

# class Object:
#     def __innit__(self, ):
#         forces = []
#     image = 
#     rect = rect()
#     def draw():
#         for i in forces:
#             rectx += forces.calculate()
#             recty += forces.calculate()

class Force:
    def __init__(self, mag, dir):
        self.__dx = 0
        self.__dy = 0
        self.__mag = mag
        self.__dir = dir
        self.calculate()

    def getDx(self):
        return self.__dx
    def getDy(self):
        return self.__dy

    def setMag(self, mag):
        self.__mag = mag
        self.calculate()

    def setDir(self, dir):
        self.__dir = dir
        self.calculate()

    def calculate(self):
        self.__dx = np.cos(np.deg2rad(self.__dir)) * self.__mag
        self.__dy = np.sin(np.deg2rad(self.__dir)) * self.__mag

        


force = Force(4, 20)

print(force.getDx(), force.setMag(6), force.getDy())


