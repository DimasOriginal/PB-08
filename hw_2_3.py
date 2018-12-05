print("FACTORYAL")
rezult = 1
num = float(input("Enter factorial value(natural number or 0): "))

#Проверка числа на натуральность или 0
while num < 0 or num % 1 != 0:
    num = float(input("Enter natural number or 0: "))

#Подсчет факториала. Исключение 0!
if num == 0:
    rezult = 1
elif num > 0:
    num = int(num)
    for i in range(1, int(num) + 1):
        rezult = rezult * i

print("Factorial {}! = {}".format(num,rezult))
