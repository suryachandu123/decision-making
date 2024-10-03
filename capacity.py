'''
There are 3 labs in the CSE department. The labs are L1, L2, and L3 with a seating capacity of x, y, and z respectively. A single lab needs to be allocated to a class of 'n' students. The labs need to be utilized to the maximum i.e the number of systems used should not be minimal. Which lab needs to be allocated to this class?
Input format:
Input consists of 4 integers
The first input denotes 'x'
The second input denotes 'y'
The third input denotes 'z'
The fourth input denotes 'n'
Output format:
Print the lab which is suitable for  'n' number of students
Refer the Sample output for formatting
Sample Input:
30
40
20
25
Sample Output:
L1
'''
# Input the seating capacities and the number of students
x = int(input("Enter seating capacity of L1:\n"))  # Capacity of L1
y = int(input("Enter seating capacity of L2:\n"))  # Capacity of L2
z = int(input("Enter seating capacity of L3:\n"))  # Capacity of L3
n = int(input("Enter the number of students:\n"))  # Number of students

# Initialize variables to hold the suitable lab and maximum capacity
suitable_lab = None
max_capacity = -1

# Check each lab's capacity and find the one that can accommodate 'n' students
if x >= n and x > max_capacity:
    suitable_lab = "L1"
    max_capacity = x

if y >= n and y > max_capacity:
    suitable_lab = "L2"
    max_capacity = y

if z >= n and z > max_capacity:
    suitable_lab = "L3"
    max_capacity = z

# Output the suitable lab or a message if none can accommodate the students
if suitable_lab:
    print(suitable_lab)
else:
    print("No lab can accommodate the given number of students")
