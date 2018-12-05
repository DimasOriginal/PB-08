print("Quadratic equation")
# Вввод данных
a = float(input("Enter 'a': "))
b = float(input("Enter 'b': "))
c = float(input("Enter 'c': "))
# Проверка что первый элемент уравнения не равен нулю.
if a == 0:
    print("Its not quadratic equation:\n"
          "x = {}".format(c / b))
# Обозначаем формулы : d - дискриминант, х1 и х2 - корни, соответственно
else:
    d = b**2 - 4 * a * c
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
#Вывод результата
    if d > 0:
        print("There are two real root:\n"
              "x1 = {}\n"
              "x2 = {}".format(x1,x2))
    elif d == 0:
        print("There is one real root (a repeated or double root:)\n"
              "x1 = x2 = {}".format(x1))
    else: #d < 0
        print("There are two distinct (non-real) complex roots:\n"
              "x1 = {}\n"
              "x2 = {}".format(x1,x2))