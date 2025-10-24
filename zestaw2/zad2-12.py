# Zbudować string stworzony z pierwszych znaków wyrazów ze stringu line.
# Zbudować napis stworzony z ostatnich znaków wyrazów ze stringu line.

def first_last(line):
    lines = line.split()
    first_chars = ''.join(word[0] for word in lines)
    last_chars = ''.join(word[-1] for word in lines)
    return first_chars, last_chars

def main():

    line = "MashuP AgencY SuggesT TougH EspressO RegaiN"
    expected_first, expected_last = 'MASTER', 'PYTHON'
    assert first_last(line)[0] == expected_first
    assert first_last(line)[1] == expected_last


if __name__ == '__main__':
    main()