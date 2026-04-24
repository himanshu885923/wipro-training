# Create and Use a Custom Package:
# Create a package called my_math with two modules: arithmetic.py and geometry.py.
# In arithmetic.py, define functions for addition, subtraction, multiplication, and division.
# In geometry.py, define functions to calculate the area of a circle and the area of a
# rectangle.
# Write a program that imports these functions from the my_math package and uses
# them to perform various calculations

from myMath import (
sum_values, diff_values, product_values, quotient_values, area_circle, area_rectangle
)

a, b = 12, 4

print("Sum: " , sum_values(a, b))
print("Difference:", diff_values(a, b))
print("Product:", product_values(a, b))

div_result = quotient_values(a, b)

if div_result is None:
    print("Division is not possible")
else:
    print("Divison:", div_result)

radius = 5
length , width = 8 ,3
print("Arrea of circle:", area_circle(radius))
print("Area of rectangle:", area_rectangle(length, width))