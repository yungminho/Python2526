# Znaleźć:
# (a) najdłuższy wyraz,
# (b) długość najdłuższego wyrazu w stringu line.

def longest_word(line):
    words = line.split()
    longest_word = max(words,key=len)
    return longest_word, len(longest_word)

def main():
    line = "najdłuższe slowo ma dziesięć znaków"
    expected_word, expected_length = 'najdłuższe', 10
    assert longest_word(line)[0] == expected_word
    assert longest_word(line)[1] == expected_length

if __name__ == '__main__':
    main()