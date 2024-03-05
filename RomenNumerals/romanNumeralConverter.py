roman_num = input("Please enter roman number between 1 and 4999: ")

int_num = 0

for i in range(len(roman_num)):
    char = roman_num[i].upper()  # Convert to uppercase for comparison
    if char == 'I':
        int_num += 1
    elif char == 'V':
        int_num += 5
    elif char == 'X':
        int_num += 10
    elif char == 'L':
        int_num += 50
    elif char == 'C':
        int_num += 100
    elif char == 'D':
        int_num += 500
    elif char == 'M':
        int_num += 1000
    else:
        print("Invalid entry")
        int_num = ''  # Reset to NULL for invalid input
        break  # Exit the loop

print(int_num)
