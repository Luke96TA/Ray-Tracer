import Vec3 as V
class ray():
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction
    def orig(self):
        return self.origin
    def dir(self):
        return self.direction
    def at(self, t):
        return V.vec3.add(self.orig(), V.vec3.constmulti(self.dir(), t))
    