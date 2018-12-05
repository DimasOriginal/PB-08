print("Fibonacci\n"
      "---------")

num = float(input("Enter Fibonacci number(natural number): "))
num1 = 1 #Первый элемент Фибоначчи
num2 = 1 #Второй элемент Фибоначчи
#Проверка числа на натуральность
while num <= 0:
    num = float(input("Enter natural number: "))
#Приводим num к целому числу
num = int(num)
#Подсчет числа Фибоначчи
if num <= 2:
    rezult = 1
else:
    sum = 2
    while sum < num:
        rezult = num1 + num2
        num1 = num2
        num2 = rezult
        sum += 1
print("{} number of Fibonacci number is {}".format(num,rezult))









#    for i in range(0, num + 1):  # Считаем число ряда Фибоначи
#        sum = sum + rezult
#        rezult = sum - rezult

#print(rezult)


# rezult = 2
# while rezult < num:
#     sum = num1 + num2
#     num1 = num2
#     num2 = sum
#     rezult += 1
#
# print(rezult)