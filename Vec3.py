from math import sqrt

class vec3():
    def __init__ (self, e0, e1, e2):
        self.e0 = e0
        self.e1 = e1
        self.e2 = e2
    def x(self):
        x = self.e0
        return x
    def y(self):
        y = self.e1
        return y
    def z(self):
        z = self.e2
        return z
    def constmulti(self, t):
        x = self.e0 * t
        y = self.e1 * t
        z = self.e2 * t
        return vec3(x, y, z)
    def add(self, v):
        x = self.e0 + v.e0
        y = self.e1 + v.e1
        z = self.e2 + v.e2
        return vec3(x, y, z)
    def negative(self):
        return self.constmulti(-1)
    def subtract(self, v):
        x = self.e0 - v.e0
        y = self.e1 - v.e1
        z = self.e2 - v.e2
        return vec3(x, y, z)
    def divide(self, t):
        x = self.e0 / t
        y = self.e1 / t
        z = self.e2 / t
        return vec3(x, y, z)
    def length_squared(self):
        return (self.e0*self.e0 + self.e1*self.e1 + self.e2*self.e2)
    def length(self):
        return sqrt(self.length_squared())
    def out(self):
        print(str(self.e0) + " " + str(self.e1) + " " + str(self.e2))
    def vecmulti(self, v):
        return vec3(self.e0*v.e0, self.e1*v.e1, self.e2*v.e2) 
    def dot(self, v):
        x = self.e0 * v.e0
        y = self.e1 * v.e1
        z = self.e2 * v.e2 
        return (x + y + z)
    def cross(self, v):
        return vec3(self.e1 * v.e2 - self.e2 * v.e1, self.e2 * v.e0 - self.e0 * v.e2, self.e0 * v.e1 - self.e1 * v.e0)
    def unit_vector(self):
        return self.divide(self.length())