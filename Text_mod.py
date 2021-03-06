# -*- coding: utf-8 -*-

form = input("Учитывать тип файла (.txt) при работе? y/n(д/н): ")
form = str(form)

try:
    # Уточение типа файла для работи с ним
    if form == "y" or form == "Y" or form == "д" or form == "Д":
        old = open(u'Normal text.txt',"r")
        new_file = open(u'New text.txt' , 'w')

    elif form == "n" or form == "N" or form == "н" or form == "Н":
        old = open(u'Normal text',"r")
        new_file = open(u'New text' , 'w')

    else:
        print("")
        print("НЕ КОРРЕКТНАЯ КОМАНДА")

    Old = old.read() # Откритие файла для чтения
    print("")
    print("Если вы хотите удалить слово из текста - запишите его в первую строку, а вторую оставьте пустой")
    print("")
    dele = input("Введите слово,котрое вы хотите заменить: ")

    cou = Old.count(dele) #Проверка наличия введеного слова/числа/символа в тексте

    if cou == 0:
        print("")
        print(" ---------------------------------------------------")
        print("|         НЕ НАЙДЕНО ТАКОГО СЛОВА В ТЕКСТЕ         |")
        print(" ---------------------------------------------------")
        print("")

    else:
        past = input("Введите слово которое заменит старое: ")
        new = Old.replace(str(dele),str(past)) # Замена слова или т.п. (dele) на past
        new_file.write(new) # Запись изменённого текста в новый файл

        # Закрытие файлов
        new_file.close()
        old.close()

        print("")
        print("---------------------------------------------------")
        print("|                Текст редактирован                |")
        print("---------------------------------------------------")
        print("")

# Происходит если не было найдено файла с начальным текстом
except FileNotFoundError:
    print("")
    print("НЕ НАЙДЕНО ФАЙЛА С НАЧАЛЬНЫМ ТЕКСТОМ")
    print("")
    print("ВОЗМОЖНЫЕ ПРОБЛЕМЫ: ")
    print("")
    print('    - ОТСУТСТВИЕ ФАЙЛА С ИМЕНЕМ "Normal text" В ОДНОЙ ПАПКЕ С ИСПОЛНЯЕМЫМ ФАЙЛОМ')
    print("    - НЕ ВЕРНО УКАЗАН ТИП ФАЙЛА")
    print("")

# Убирает оповещение о NameError если было введено не корректное значение в вопросе с учитиванием типа файла
except NameError:
    print("")
