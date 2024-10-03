'''
Write a program to determine the fee amount to be collected from a student. 
Refer the table below for fee details.
  Student Type  
  Student Type denoted as  
  Fee Details  
Merit Seat Day Scholar
MSDS

Tuition fee + Bus fee



Merit Seat Hosteller
MSH
Tuition fee + Hostel fee

Management Seat Day Scholar



MGSDS

150% of Tuition fee + Bus fee



Management Seat Hosteller
MGSH

150% of Tuition fee + Hostel fee




Input format:
The first input corresponds to the student type
The second input corresponds to the tuition fee
The third input corresponds to the bus fee or hostel fees
Output format:
Print the total fee amount of the corresponding student with 2 decimal places.
Refer below sample output for formatting
Sample Input:
MSH
40000
50000
Sample Output:
90000.00
'''
# Input for student type
student_type = input("Enter student type (MSDS, MSH, MGSDS, MGSH):\n").strip()

# Input for tuition fee
tuition_fee = float(input("Enter the tuition fee:\n"))

# Input for bus fee or hostel fee
other_fee = float(input("Enter the bus fee or hostel fee:\n"))

# Initialize total_fee variable
total_fee = 0.0

# Calculate total fee based on student type
if student_type == "MSDS":
    total_fee = tuition_fee + other_fee  # Tuition fee + Bus fee
elif student_type == "MSH":
    total_fee = tuition_fee + other_fee  # Tuition fee + Hostel fee
elif student_type == "MGSDS":
    total_fee = (1.5 * tuition_fee) + other_fee  # 150% of Tuition fee + Bus fee
elif student_type == "MGSH":
    total_fee = (1.5 * tuition_fee) + other_fee  # 150% of Tuition fee + Hostel fee
else:
    print("Invalid student type")
    exit()  # Exit if the student type is invalid

# Output the total fee amount with 2 decimal places
print(f"{total_fee:.2f}")
