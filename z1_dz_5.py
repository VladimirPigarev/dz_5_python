# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
input_text = 'Привет, абвиатура содержит абв?'
print(input_text)
res_text = input_text.split(' ') # разбиваем строку на слова
fragment = 'абв' # искомый фрагмент в слове
new_mas = [] 
for i in res_text:
    if fragment not in i: # условие, при котором проверяется, содержится ли фрагмент в слове.
        new_mas.append(i) # создаем список из слов, не содержащих заданный фрагмент
print(new_mas)
itog = ' '.join(new_mas) # преобразуем список в строку опять
print(itog)
my_file = open('file.txt', 'w+', encoding="utf-8") # создаем файл
my_file.write(itog) # записываем в файл итог прошлых действий
my_file.close()