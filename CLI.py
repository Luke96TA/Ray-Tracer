import Vec3 as V
import color as C
import ray
import hittable as hit
import hittable_list as hlist
import rtweekend
from math import inf
from math import sqrt
point3 = V.vec3
color = V.vec3

aspect_ratio = 16/9
image_width = int(400)

def ray_color(r, world):
    rec = hit.hit_record()
    if (world.hit(r, 0, inf, rec)):
        return V.vec3.divide(V.vec3.add(rec.normal, color(1, 1, 1)), 2)
    else:
        unit_direction = V.vec3.unit_vector(ray.ray.dir(r))
        a = 0.5*(V.vec3.y(unit_direction) + 1)
        return V.vec3.add(V.vec3.constmulti(color(1.0, 1.0, 1.0), 1.0 - a), V.vec3.constmulti(color(0.5, 0.7, 1.0), a))



#Calculate Image Height
image_height = int(image_width/aspect_ratio)
if image_height < 1:
    image_height = 1

world = hlist.hittable_list()
world.add(hit.sphere(point3(0, 0, -1), 0.5))
world.add(hit.sphere(point3(0, -100.5, -1), 100))

#Camera
focal_length = 1.0
viewport_height = 2.0
viewport_width = viewport_height * (image_width/image_height)
camera_center = point3(0, 0, 0)

#Caculate the vectors across the horizontal and down the vertical viewport edges
viewport_u = V.vec3(viewport_width, 0, 0)
viewport_v = V.vec3(0, -viewport_height, 0)

#Calculate the horizontal and vertical delta vectors from pixel to pixel.
pixel_delta_u = V.vec3.divide(viewport_u, image_width)
pixel_delta_v = V.vec3.divide(viewport_v, image_height)

#Calculate location of the upper left pixel
viewport_upper_left = V.vec3.subtract(V.vec3.subtract(camera_center, V.vec3(0, 0, focal_length)), V.vec3.divide(V.vec3.add(viewport_u, viewport_v), 2))
pixel100_loc = V.vec3.add(viewport_upper_left, V.vec3.divide(V.vec3.add(pixel_delta_u, pixel_delta_v), 2))



#Rendering
f = open('Image.ppm','w')
f.write("P3\n")
f.write(str(image_width) + " "+ str(image_height) + "\n")
f.write("255" + "\n")
f.close()
for j in range(0, image_height):
    print("Scanline remaining: " + str(image_height - j))
    for i in range(0, image_width):
        pixel_center = V.vec3.add(pixel100_loc, V.vec3.add(V.vec3.constmulti(pixel_delta_u, i), V.vec3.constmulti(pixel_delta_v, j)))
        ray_direction = V.vec3.subtract(pixel_center, camera_center)
        r = ray.ray(camera_center, ray_direction)
        pixel_color = ray_color(r, world)
        C.write_color(pixel_color)
print("Done")
