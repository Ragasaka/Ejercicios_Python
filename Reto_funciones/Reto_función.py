def print_text_number (str1, str2) :

    number_counter = 0

    for x in range(1,101,1) :
        if((x % 15) == 0):                  # Se cheque si es un multiplo de 15
            print(str1, str2)
        elif ((x % 5) == 0):                # Se cheque si es un multiplo de 5
            print(str2)
        else: 
            if ((x % 3) == 0):              # Se cheque si es un multiplo de 3
                print(str1)
            else :                          # Si los chequeos fallan, entonces imprime el número
                print(x)
                number_counter += 1

    return number_counter


numbers = print_text_number('Hola','Mundo')

print(f'Se imprimieron {numbers} números')