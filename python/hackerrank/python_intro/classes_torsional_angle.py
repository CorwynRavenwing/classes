import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        return

    def __sub__(self, no):
        return Points(
            self.x - no.x,
            self.y - no.y,
            self.z - no.z
        )

    def dot(self, no):
        Xs = self.x * no.x
        Ys = self.y * no.y
        Zs = self.z * no.z
        return Xs + Ys + Zs

    def cross(self, no):
        Ax = self.x
        Ay = self.y
        Az = self.z
        Bx = no.x
        By = no.y
        Bz = no.z
        return Points(
            Ay*Bz - Az*By,
            Ax*Bz - Az*Bx,
            Ax*By - Ay*Bx
        )
        
    def absolute(self):
        X2 = self.x ** 2
        Y2 = self.y ** 2
        Z2 = self.z ** 2
        return pow((X2 + Y2 + Z2), 0.5)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))

