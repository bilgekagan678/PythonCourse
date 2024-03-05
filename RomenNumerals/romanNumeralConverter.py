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

if roman_num in roman_dict.keys():
    print(roman_dict.get(roman_num))
