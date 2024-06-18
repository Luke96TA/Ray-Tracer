import hittable


class hittable_list():
    def __init__(self):
        self.hittable_list = []
    def clear(self):
        self.hittable_list = []
    def add(self, object):
        self.hittable_list.append(object)
    def hit(self, r, ray_tmin, ray_tmax, rec):
        temp_rec = hittable.hit_record()
        hit_anything = False
        closest_so_far = ray_tmax
        for object in self.hittable_list:
            if hittable.sphere.hit(object, r, ray_tmin, closest_so_far, temp_rec):
                hit_anything = True
                closest_so_far = temp_rec.t
                rec = temp_rec
        return hit_anything, rec