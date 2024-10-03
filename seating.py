'''
There are 3 labs in the CSE department are L1, L2, and L3 with a seating capacity of x, y, and z. A single lab needs to be allocated to a class of 'n' students. How many of the 3 labs can accommodate 'n' students?
Input format:
Input consists of 4 integers
The first input denotes the seating capacity of L1(a)
The second input denotes the seating capacity of L2(b)
The third input denotes the seating capacity of L3(c)
The fourth input denotes the number of students(x)
Output format:
Print the number of labs which can accommodate the 'n' number of students
Refer the Sample output for formatting
Sample Input:
30
40
20
25
Sample Output:
2 
'''
# Input the seating capacities and the number of students
L1_capacity = int(input("Enter seating capacity of L1:\n"))
L2_capacity = int(input("Enter seating capacity of L2:\n"))
L3_capacity = int(input("Enter seating capacity of L3:\n"))
number_of_students = int(input("Enter the number of students:\n"))

# Initialize the count of labs that can accommodate the students
accommodating_labs = 0

# Check each lab's capacity and count how many can accommodate the students
if L1_capacity >= number_of_students:
    accommodating_labs += 1
if L2_capacity >= number_of_students:
    accommodating_labs += 1
if L3_capacity >= number_of_students:
    accommodating_labs += 1

# Print the number of labs that can accommodate the students
print(accommodating_labs)
