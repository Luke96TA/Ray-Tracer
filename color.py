import Vec3 as V

def write_color(c):
    f = open('Image.ppm','a')
    r = (V.vec3.x(c))
    g = (V.vec3.y(c))
    b = (V.vec3.z(c))
    ir = int(255.9999 * r)
    ig = int(255.9999 * g)
    ib = int(255.9999 * b)
    f.write(str(ir) + " "+ str(ig)+ " " + str(ib) + "\n")
    f.close()