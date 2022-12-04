# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open("file1.txt", "r") as my_file1:
    str1 = my_file1.read()
my_file1.close()
string = str1
def coding(string):
    cout = 1
    for i in range(len(string)-1):
        if i <= len(string):
            if string[i] == string[i + 1]:
                cout += 1
            else:
                a = string[i]
                print(cout, string[i])
                cout = 1
    print(cout, string[i])
coding(string)