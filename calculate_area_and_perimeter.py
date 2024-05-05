# Write two functions to calculate the area and perimeter of a rectangle.

# Use the functions to calculate the area and perimeter of given dimensions.

def area_of_rectangle(l1, b1):
    area = l1 * b1
    return area

def peri_of_rectangle(l1, b1):
    perimeter = 2*(l1+b1)
    return perimeter

l1 = int(input("Enter the length - "))
b1 = int(input("Enter the breadth - "))

area = area_of_rectangle(l1, b1)
perimeter = peri_of_rectangle(l1, b1)

print('Area of Rectangle is - ', area)
print('Perimeter of Rectangle is - ', perimeter)
