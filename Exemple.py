"""Задача №49. Решение в группах
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной"""

# menu = ['first name', 'last name', 'number']
# save = ['Иван', 'Иванов', '89156784598']
# memory = ["Долгов", "Андрей", "89564367890"]
collect = {}
d=1
with open('phonebook.txt', 'r', encoding='utf-8') as file:       #Прочитать из файла
    for l in file:
        l = l.replace('\n','')
        collect[d] = list(l.split(';'))
        d+=1
dict = collect
path = 'phonebook.txt'
#for i in dict:                 #Поиск Фамилии
    # print(dict[i])
    # for j in range(1):
    #print(dict[i][0])
# for i in dict:                  #поиск по фамилии
#     if dict[i][0] == "Иванов":
#         print(dict[i])
# for i in dict:                    #Поиск по части текста(в нашем случае "89")
#     for j in range(3):
#         if "89" in dict[i][j]:
#             print(dict[i])
# for i in dict:                    #Поиск по части текста(в нашем случае буква "в")
#     for j in range(3):
#         if "в" in dict[i][j]:
#             print(dict[i])
print("Здравствуйте ")
print("Для того чтобы вывести телефонную книгу, нажмите - 1")
print("Для вывода фамилий, нажмите - 2 ")
print("Для того чтобы добавить запись, нажмите - 3")
print("Для того чтобы изменить контакт, нажмите - 4")
print("Для того чтобы удалить контакт, нажмите - 5")
n = input(str())
if n == "1":
    print(dict)
if n == "2":
    for i in dict:                 #Вывод Фамилий
        for j in range(1):
            print(dict[i][0])
if n == "3":
    s=1
    save = list(input("Введите Фамилию, Имя и телефон через пробел ").split())
    while True:
        if s in dict:
            s+=1
        else:
            dict[s] = save
            break
    print(dict)
if n == "4":
    print("Введите фамилию для поиска контакте: ")
    fio = input(str())
    for i in dict:                  #поиск по фамилии 
        if dict[i][0] == fio:
            print(dict[i])
            print("Вы хотите изменить Фамилию? нажмите 1")
            print("Вы хотите изменить Имя? нажмите 2")
            print("Вы хотите изменить телефон? нажмите 3")
            vib = input(str())
            if vib == "1":
                print("Введите новую фамилию: ")
                fioChange = input(str().split())
                dict[i][0] = fioChange
                print(dict[i])
            if vib == "2":
                print("Введите новое имя: ")
                fioChange = input(str().split())
                dict[i][1] = fioChange
                print(dict[i])
            if vib == "3":
                print("Введите новый телефон: ")
                fioChange = input(str().split())
                dict[i][2] = fioChange
                print(dict[i])
        else:
            print("Контакт с указанными данными не найден")
if n == "5":
    print("Введите фамилию для поиска контакте: ")
    fio = input(str())
    for i in dict:                  #поиск по фамилии 
        if dict[i][0] == fio:
            print(dict[i])
            print("Вы точно хотите удалить контакт? нажмите 1")
            print("Если вы передумали удалять контакт, нажмите 2")
            q = input(str())
            if q == "1":
                del dict[i]
                print("Контакт удален")
                print(dict)
                break
            if q == "2":
                pass
                
    
with open('phonebook.txt', 'w', encoding='utf-8') as file:    # запись в файл
    for k in dict:
        file.write(f'{dict[k][0]};{dict[k][1]};{dict[k][2]}\n')
# collect = {}
# d=1
# with open('phonebook.txt', 'r', encoding='utf-8') as file:       #Прочитать из файла
#     for l in file:
#         l = l.replace('\n','')
#         collect[d] = list(l.split(';'))
#         d+=1
#         #collect.append(list(l.split(';')))
# print(collect)