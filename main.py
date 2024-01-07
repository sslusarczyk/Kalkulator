import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')


operation = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"))
if operation == 2 or operation == 4:
    number1 = int(input("Podaj skladnik 1. "))
    try:
        number1_integer = int(number1)
    except ValueError:
        print("Nie jest liczba prosze wprowadzić liczbę.")
        exit(1)

    number2 = int(input("Podaj skladnik 2. "))
    try:
        number2_integer = int(number2)
    except ValueError:
        print("Nie jest liczba prosze wprowadzić liczbę.")
        exit(1)
    if operation == 2:
        logging.info("Odejmuję %s i %d " %(number1,number2))
        result = number1 - number2
    elif operation == 4:
        logging.info("Dzielę %s i %d " %(number1,number2))
        result = number1 / number2
    else:
        print("Nie ma takiej operacji")
        exit(1)
else:
    pass

        
if operation == 1 or operation == 3:
    if operation == 1:
            result = 0
            while True:
                number = input("Podaj skladnik lub exit ")
                if number.lower() == 'exit':
                      break # Wyjscie z pętli
                try:
                      number = int(number)
                      result += number
                      logging.info("Dodaję %s " %(number))
                      logging.info("Obecny wynik %s " %(result))

                except ValueError:
                       print("Nie jest liczba prosze wprowadzić liczbę.")
                       exit(1)
                
    elif operation == 3:
            result = 1
            while True:
                number = input("Podaj skladnik lub exit ")
                if number.lower() == 'exit':
                      break # Wyjscie z pętli
                try:
                      number = int(number)
                      result *= number
                      logging.info("Mnożę %s " %(number))
                      logging.info("Obecny wynik %s " %(result))
                except ValueError:
                       print("Nie jest liczba prosze wprowadzić liczbę.")
                       exit(1)
    else:
            print("Nie ma takiej operacji")
            exit(1)
else:
    pass

print("Wynik to %s" % str(result))





