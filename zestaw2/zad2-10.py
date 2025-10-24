# Mamy dany string wielowierszowy line.
# Podać sposób obliczenia liczby wyrazów w stringu.
# Przez wyraz rozumiemy ciąg "czarnych" znaków, oddzielony
# od innych wyrazów białymi znakami (spacja, tabulacja, newline).

def count_words(line):
    return len(line.split())

def main():
    line = """Lorem     ipsum dolor sit amet, consectetur adipiscing elit. 
            Quisque nec venenatis mauris.
            Quisque dignissim eget sapien sit  amet finibus. Vivamus at bibendum ipsum. 
            Quisque ultricies nisi urna, sit amet faucibus nibh tincidunt sed. 
            Aenean mollis molestie  lectus nec suscipit. Nullam tempus quam eu condimentum sagittis. \n
            Vivamus id ultrices augue, ac efficitur augue. 
            Nulla accumsan leo    nec mauris pretium, et sodales est malesuada. 
            In et est ut               augue condimentum cursus. Aliquam ac consectetur libero. \n 
            Nulla et lacus ipsum. In volutpat, orci at accumsan placerat, 
            sem diam dictum lorem,   finibus ultrices ex libero ac nunc."""

    assert count_words(line) == 93

if __name__ == '__main__':
    main()