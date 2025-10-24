# Posortować wyrazy ze stringu line raz alfabetycznie,
# a raz pod względem długości. Wskazówka: funkcja wbudowana sorted().

def sort_string(line):
    words = line.split()
    return sorted(words), sorted(words, key=len)

def main():
    line = "Aaaaaa Bbbbb Cccc Ddd Ee F"
    expected_alpha = ['Aaaaaa', 'Bbbbb', 'Cccc', 'Ddd', 'Ee', 'F']
    expected_length = ['F', 'Ee', 'Ddd', 'Cccc', 'Bbbbb', 'Aaaaaa']
    assert sort_string(line)[0] == expected_alpha
    assert sort_string(line)[1] == expected_length

if __name__ == '__main__':
    main()
