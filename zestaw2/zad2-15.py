# Na liście L znajdują się liczby całkowite dodatnie.
# Stworzyć string będący ciągiem cyfr kolejnych liczb z listy L.

def number_sequence(list):
    return ''.join(str(number) for number in list)

def main():
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = '12345678910'
    assert number_sequence(L) == expected
if __name__ == '__main__':
    main()