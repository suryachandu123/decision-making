'''
Write a program to check whether the given character is vowel or consonant.
Input format:
The input consist of a character
Output format:
The output consists of a below-given string
“Vowel” / “Consonant” / “Not an alphabet”
Sample Input:
e

Sample Output:
Vowel
'''
# Input a character
char = input("Enter a character:\n")

# Check if the input is a single alphabet character
if len(char) == 1 and char.isalpha():
    # Convert character to lowercase for easier comparison
    char_lower = char.lower()
    
    # Check if the character is a vowel
    if char_lower in 'aeiou':
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Not an alphabet")
