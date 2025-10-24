# W tekście znajdującym się w stringu line
# zamienić ciąg znaków "GvR" na "Guido van Rossum".

def change_abbr(line, abbr, full):
    return line.replace(abbr, full)


def main():
    line = """GvR born 31 January 1956 is a Dutch programmer.
            GvR is the creator of the Python programming language, for which GvR was the 
            benevolent dictator for life" (BDFL) until GvR stepped down from the position on 12 July 2018.
            GvR remained a member of the Python Steering Council through 2019, 
            and GvR withdrew from nominations for the 2020 election."""

    expected_line = """Guido van Rossum born 31 January 1956 is a Dutch programmer.
            Guido van Rossum is the creator of the Python programming language, for which Guido van Rossum was the 
            benevolent dictator for life" (BDFL) until Guido van Rossum stepped down from the position on 12 July 2018.
            Guido van Rossum remained a member of the Python Steering Council through 2019, 
            and Guido van Rossum withdrew from nominations for the 2020 election."""
    assert change_abbr(line, 'GvR', 'Guido van Rossum') == expected_line

if __name__ == '__main__':
    main()