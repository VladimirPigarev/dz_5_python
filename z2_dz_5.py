# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
import random
from random import randint

igrok1 = input("Игрок № 1, представтесь: ")
igrok2 = input("Игрок № 2, представтесь: ") # igrok2 = "РОБОКОП" (для игры с ботом)
konfety = int(input("количество конфет на столе: ")) # konfety = int(random.randint(100, 200)) (для игры с ботом)

marker = randint(0,2) 
if marker:
    print(f"Первый ходит {igrok1}")
else:
    print(f"Первый ходит {igrok2}")

count1 = 0 
count2 = 0

def input_konfety(name): # функция для ввода количества конфет пользователем
    n = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while n < 1 or n > 28:
        n = int(input(f"{name}, введите корректное количество конфет: "))
    return n


def step(name, k, count, konfety): # функция подсчета остатка
    print(f"Ходил {name}, он взял {k}, теперь у него {count}. Осталось на столе {konfety} конфет.")

while konfety > 28:
    if marker:
        k = input_konfety(igrok1)
        count1 += k
        konfety -= k
        marker = False
        step(igrok1, k, count1, konfety)
    else:
        k = input_konfety(igrok2) # k = random.randint(1, 28) для игры с ботом
        count2 += k
        konfety -= k
        marker = True
        step(igrok2, k, count2, konfety)

if marker:
    print(f"Выиграл {igrok1}")
else:
    print(f"Выиграл {igrok2}")