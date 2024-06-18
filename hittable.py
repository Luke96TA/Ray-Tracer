import ray
import Vec3 as V
from math import sqrt
point3 = V.vec3


class hit_record():
    def __init__(self):
        self.p  = V.vec3(0, 0, 0)
        self.normal = V.vec3(0, 0, 0)
        self.t = 0
    def set_face_normal(self, r, outward_normal):
        front_face = (V.vec3.dot(ray.ray.dir(r), outward_normal) < 0)
        if front_face:
            self.normal = outward_normal
        else:
           self.normal = V.vec3.negative(outward_normal)


class sphere():
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    def hit(self, r, ray_tmin, ray_tmax, rec):
        oc = V.vec3.subtract(self.center, ray.ray.orig(r))
        a = V.vec3.length_squared(ray.ray.dir(r))
        h = V.vec3.dot(ray.ray.dir(r), oc)
        c = V.vec3.length_squared(oc) - self.radius*self.radius
        discriminant = h*h - a*c
        if discriminant < 0:
           return False  
        sqrtd = sqrt(discriminant)
        root = (h - sqrtd) / a
        if root <= ray_tmin or root >= ray_tmax:
            root = (h + sqrtd)/a
            if root <= ray_tmin or root >= ray_tmax:
                return False
        rec.t = root
        rec.p = r.at(rec.t)
        rec.normal = V.vec3.divide(V.vec3.subtract(rec.p, self.center), self.radius)
        outward_normal = V.vec3.divide(V.vec3.subtract(rec.p, self.center), self.radius)
        rec.set_face_normal(r, outward_normal)
        return True




