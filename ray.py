import Vec3 as V
def copy(vec):
    return V.vec3(V.vec3.x(vec), V.vec3.y(vec), V.vec3.z(vec))
class ray():
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction
    def orig(self):
        return self.origin
    def dir(self):
        return self.direction
    def at(self, t):
        return V.vec3.add(copy(self.orig()), V.vec3.constmulti(copy(self.dir()), t))
    