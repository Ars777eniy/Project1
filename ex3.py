import math
a = 1.774
x = -2.7
m = 5
n = 1
y = (math.sqrt(a + (n ** 2) * (x ** 2))) / ((a + x) * m)
print(y)

if abs(y) < 1:
    z = y + 1
else:
    z = math.cos(y**2)
print(z)