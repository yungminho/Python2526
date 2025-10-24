# Znaleźć łączną długość wyrazów w stringu line.
# Wskazówka: można skorzystać z funkcji sum().

def sum_char(line):
    return sum(len(word) for word in line.split())

def main():
    line = 'Ten tekst ma dokładnie czterdzieści jeden liter'
    expected = 41
    assert sum_char(line) == expected


if __name__ == '__main__':
    main()