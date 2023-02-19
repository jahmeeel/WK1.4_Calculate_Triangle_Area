'''
Write a Python program that calculates the area of a triangle given its base and 
height.

Expected output: The area of the triangle, rounded to 2 decimal places.
'''

'''
Understand the Problem:
- Write a Python program that calculates the area of a triangle given its base and height.
- I have to multiply the base and height and divide by 2 to get the area.


- Input:
    - The base of the triangle.
    - The height of the triangle.

- Output:
    - The area of the triangle, rounded to 2 decimal places.

Problem Breakdown:
    - Store the base and height in variables.
    - Calculate the area of the triangle using arithmetic operators.
    - Print the area of the triangle to the screen.

Execute the Plan

Review:
- I learned that in order to control the precision of the output,I can use the round built-in function to control how many decimal places the output is rounded to.


'''

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = (base * height) / 2
print(f"The area of the triangle is {round(area, 2)}")
