# Водим значения (по умолчанию float)
a = float(input("Enter 'a': "))
b = float(input("Enter 'b': "))
rezult = 0

# Проверка что число окончания ряда больше начала
while a > b:
    b = float(input("Enter 'b' (biggest num that 'a'): "))

# округляем число "а" с помощью int ("отрезая" часть за точкой), для положительных чисел с плавающей точкой после
# использования int прибавляем 1 чтобы отсчет начинался со следюющего числа
if a % 1 == 0 or a < 0:
    a = int(a)
else:
    a = int(a) + 1
# b просто округляем приводя к int
b = int(b)
#сумма всех натуральных чисел, к b добавляем 1 чтобы было включительно с b
for i in range(a,b+1):
    if i > 0:
        rezult = rezult + i

if rezult == 0:
    print("Your row havent natural numbers")
else:
    print("The sum of the natural numbers: ",rezult)