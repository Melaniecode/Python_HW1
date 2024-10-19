import math

class Sphere:
    def __init__(self, r):
        self.radius = r
    
    def volume(self):
        return (4/3) * math.pi * self.radius**3
      
    def surface_area(self):
        return 4 * math.pi * self.radius**2
    
    def __repr__(self):
        return f"Sphere object, radius={self.radius}"
    
    def __str__(self):
        return f"Sphere object, rad={self.radius}, volume={self.volume():.2f}, surface_area={self.surface_area():.2f}"

r = int(input("請輸入一個整數: "))
sphere = Sphere(r)

print(repr(sphere))
print(sphere)
