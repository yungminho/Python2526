# Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x (typ float)
# i wypisujący x oraz trzecią potęgę x. Zatrzymanie programu następuje po wpisaniu
# z klawiatury stop. Jeżeli użytkownik wpisze napis zamiast liczby, to program ma wypisać
# komunikat o błędzie i kontynuować pracę.

def cube(number):
    return f'Podana liczba: {number} | Trzecia potęga: {number**3}'

def main():

    while True:
        user_input = input('Podaj liczbę rzeczywistą lub wpisz \'stop\', aby zakonczyć:')

        if user_input.lower() == 'stop':
            print('program zakończony')
            break

        try:
            print(cube(float(user_input)))

        except ValueError:
            print('Błąd: Wpisano niepoprawną wartość. Proszę podać liczbę rzeczywistą.')


if __name__ == '__main__':
    main()