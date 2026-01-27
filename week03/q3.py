# Question 3 ----------------------------------------------

# tuples are ordered and unchangeable. allows duplicates
# 'pack' a tuple
point1 = (3, 5)
print(f'Point 1: {point1}')
point2 = (7, 2)
print(f'Point 2: {point2}')

x1, y1 = point1
print(f'x1 = {x1}, y1 = {y1}')
x2, y2 = point2
print(f'x2 = {x2}, y2 = {y2}')

# 𝑑 = sqrt( (𝑥2 −𝑥1)^2 + (𝑦2−𝑦1)^2 )
distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
print(f'Distance between points: {distance}')

# ------------
py_chars = tuple("PYTHON")
print(f'Characters tuple: {py_chars}')
for char in py_chars:
    print(char)
