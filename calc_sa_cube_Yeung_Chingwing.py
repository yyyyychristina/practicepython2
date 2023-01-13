'''
You can calculate the surface area of a cube if you know the length of an edge.
Write a program that takes the length of an edge (an integer) as input and prints
the cube’s surface area as output.

Remember, the surface area is the area of all sides added together. But, a with cube, all side are equal.
'''

#prompt user to enter the length
length_of_an_edge = int(input('Enter length of an edge:'))

#output
area_of_one_side = length_of_an_edge*length_of_an_edge
print('area_of_one_side:', area_of_one_side)

surface_area = area_of_one_side*6
print('surface_area:', surface_area)
