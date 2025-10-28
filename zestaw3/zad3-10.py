# Stworzyć słownik tłumaczący liczby zapisane
# w systemie rzymskim (z literami I, V, X, L, C, D, M)
# na liczby arabskie (podać kilka sposobów tworzenia takiego słownika).
# Mile widziany kod tłumaczący całą liczbę [funkcja roman2int()].

# Metody tworzenia słownika
# 1. Klasyczna definicja
roman_to_arabic_classic = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
}

# 2. Konwersja z listy krotek
roman_to_arabic_tuple = dict([('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000)])

# 3. Konwersja z dwóch list
roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
arab = [1, 5, 10, 50, 100, 500, 1000]
roman_to_arab_two_lists = dict(zip(roman, arab))

def roman2int(roman_number, roman_to_arabic):
    total = 0
    previous = 0

    for char in reversed(roman_number):
        curr = roman_to_arabic[char]

        if curr < previous:
            total -= curr
        else:
            total += curr

        previous = curr

    return total

def main():
    roman_number = ['III', 'VIII', 'CDLXXVI','MCCCLXIV', 'MMXXV']

    for roman in roman_number:
        print(f'Roman: {roman} | Integer: {roman2int(roman, roman_to_arabic_tuple)}')


if __name__ == '__main__':
    main()