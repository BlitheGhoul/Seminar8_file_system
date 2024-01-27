
from return_data_file import data_file
from rewrite import rewrite1, rewrite2
from print_data import print_file

def transfer_row():
    data, nf = data_file()
    count_rows = len(data)
    if count_rows == 0:
        print("Ошибка!Файл пустой!")
    else:
        number_row = int(input(f"Введите номер строки "
                               f"от 1 до {count_rows}: "))
        while number_row < 1 or number_row > count_rows:
            number_row = int(input(f"Ошибка!"
                                   f"Введите номер строки "
                                   f"от 1 до {count_rows}: "))
        transfering_row = data[number_row - 1]
        if count_rows > 1:
            del data[number_row - 1]
            rewrite1(data, nf)
        else:
            del data[number_row - 1]
            with open(f'db//data_{nf}.txt', 'w', encoding='utf-8') as file:
                file.writelines(data)
        if nf == 1:
            with open(f'db//data_{nf + 1}.txt', 'a', encoding='utf-8') as file:
                file.writelines(transfering_row)
            rewrite2(nf + 1)    
        else:
            with open(f'db//data_{nf - 1}.txt', 'a', encoding='utf-8') as file:
                file.writelines(transfering_row)
            rewrite2(nf - 1)
                
                
                
        print()
        print("Строка успешно перенесена!")
        print()
        print_file()
        
