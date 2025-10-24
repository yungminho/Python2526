# Na liście L mamy liczby jedno-, dwu- i trzycyfrowe dodatnie.
# Chcemy zbudować string z trzycyfrowych bloków, gdzie liczby jedno-
# i dwucyfrowe będą miały blok dopełniony zerami, np. 007, 024. Wskazówka: str.zfill().

def split_to_three_block_number(line):
    return ' '.join(str(num).zfill(3) for num in line)

def main():
    L = [1, 2, 33, 44, 555, 666]
    expected = '001 002 033 044 555 666'
    assert split_to_three_block_number(L) == expected

if __name__ == '__main__':
    main()