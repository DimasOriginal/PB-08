num1 = int(input("Enter first integer number:  "))
print("Integer - {}, realis (float) - {}, logical - {}, string - {} of your number".format(num1, float(int(num1)), bool(num1),str(num1)))
num2 = int(input("Enter second integer number:  "))

print("Two integer number: {} + {} = {}".format(int(num1), int(num2), int(num1) + int(num2)))
print("Two integer number: {} * {} = {}".format(int(num1), int(num2), int(num1) * int(num2)))

print("Two realis (float) number: {} + {} = {}".format(float(num1), float(num2), float(num1) + float(num2)))
print("Two realis (float) number: {} * {} = {}".format(float(num1), float(num2), float(num1) * float(num2)))

print("Two  string: {} + {} = {}".format(str(num1), str(num2), str(num1) + str(num2)))

print("Two  logical number: {} + {} = {}".format(bool(num1), bool(num2), bool(num1) + bool(num2)))
print("Two  logical number: {} * {} = {}".format(bool(num1), bool(num2), bool(num1) * bool(num2)))

print("One integer number with one realis (float) number: {} + {} = {}".format(int(num1), float(num2), int(num1) + float(num2)))
print("One integer number with one realis (float) number: {} * {} = {}".format(int(num1), float(num2), int(num1) * float(num2)))

print("One integer number with one logical number: {} + {} = {}".format(num1, bool(num2), num1 + bool(num2)))
print("One integer number with one logical number: {} * {} = {}".format(num1, bool(num2), num1 * bool(num2)))

print("One realis (float) number with one logical number: {} + {} = {}".format(float(num1), bool(num2), float(num1) + bool(num2)))
print("One realis (float) number with one logical number: {} * {} = {}".format(float(num1), bool(num2), float(num1) * bool(num2)))

print("One string with one logical number: {} * {} = {}".format(str(num1), bool(num2), str(num1) * bool(num2)))