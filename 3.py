# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.
# Входные данные
# Входной файл INPUT3.TXT содержит целое число N (1 < N ≤ 10^6).
# Выходные данные
# В выходной файл OUTPUT3.TXT выведите ответ на задачу.

with open("input3.txt") as inputFile:
    inputArray = [row.strip() for row in inputFile]
outputArray = inputArray
for i in range(len(inputArray)):
    for j in range(2,int(int(inputArray[i])**0.5)+1):
        if int(inputArray[i])%j==0:
            outputArray[i] = j
            break
        else:
            outputArray[i] = int(inputArray[i])
with open("output3.txt", "w") as outputFile:
    for k in range(len(outputArray)):
        outputFile.write(str(outputArray[k]) + '\n')