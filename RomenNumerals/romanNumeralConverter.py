roman_dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

roman_num = input("Please enter Roman Number between 1 and 4999: ").upper()

int_num = 0

for i in range(len(roman_num)-1):
    if roman_num[i] in roman_dict.keys():
        if roman_dict.get(roman_num[i+1]) > roman_dict.get(roman_num[i]):
            int_num -= roman_dict.get(roman_num[i])
        else:
            int_num += roman_dict.get((roman_num[i]))
    else:
        print("Please enter a valid number!")
        int_num = ''

if roman_num[-1] in roman_dict.keys():
    int_num += roman_dict[roman_num[-1]]

print(int_num)
