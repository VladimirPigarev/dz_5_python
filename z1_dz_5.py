# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
input_text = str(input("Введите текст содержащий в словах фрагмент (абв), например: Привет, абвиатура содержит абв? : ")) 
print(input_text)
res_text = input_text.split(' ')
fragment = 'абв'
new_mas = []
for i in res_text:
    if fragment not in i:
        new_mas.append(i)
print(new_mas)
itog = ' '.join(new_mas)
print(itog)
my_file = open('file.txt', 'w+', encoding="utf-8")
my_file.write(itog)
my_file.close()