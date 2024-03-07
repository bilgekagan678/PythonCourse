def roman_to_int(roman_num):
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    invalid_patterns = ["IIII", "XXXX", "CCCC", "MMMMM"]

    for pattern in invalid_patterns:
        if pattern in roman_num:
            print("Invalid Roman numeral pattern detected.")
            return None

    int_num = 0
    prev_num = 0

    for i in range(len(roman_num) - 1, -1, -1):
        if roman_num[i] in roman_dict.keys():
            curr_num = roman_dict[roman_num[i]]
            if curr_num < prev_num:
                int_num -= curr_num
            else:
                int_num += curr_num
            prev_num = curr_num
        else:
            print("Please enter a valid number!")
            return None

    return int_num


def main():
    roman = input("Please enter Roman Number between 1 and 4999: ")
    if not roman.isalpha():
        print("Please enter a valid number!")
    integer = roman_to_int(roman.upper())
    if integer:
        print(f"The Arabic integer for {roman.upper()} is {integer}")


if __name__ == "__main__":
    main()
