# Znaleźć liczbę cyfr zero w dużej liczbie całkowitej.
# Wskazówka: zamienić liczbę na string.

def find_number_of_zeros(line):
    return str(line).count('0')

def main():
    num = 1_000_000
    expected = 6
    assert find_number_of_zeros(num) == expected

if __name__ == '__main__':
    main()