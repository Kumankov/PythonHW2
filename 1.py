# На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной.
# Входные данные
# В первой строке входного файла INPUT1.TXT записано натуральное число N (1 ≤ N ≤ 100) – число монеток. 
# В каждой из последующих N строк содержится одно целое число – 1 если монетка лежит решкой вверх и 0 если вверх гербом.

# Выходные данные
# В выходной файл OUTPUT1.TXT выведите минимальное количество монет, которые нужно перевернуть.

with open("input1.txt") as inputFile:
    inputArray = [row.strip() for row in inputFile]
count1=0
count0=0
for i in range(int(inputArray[0])):
    if int(inputArray[i+1])==1:
        count1= count1+1
    else:
        count0+=1
with open("output1.txt", "w") as outputFile:
    if count1<=count0:
        outputFile.write(str(count1))
    else:
        outputFile.write(str(count0))
    