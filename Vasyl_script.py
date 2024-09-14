print("Введіть два числа, математичну дію і програма вам порахує результат")
first_num = int(input("Введіть перше число: "))
second_num = int(input("Введіть друге число: "))
math_ope = input("Введіть математичну дію: ")

if math_ope == "+":
    print("Результат:", first_num + second_num)
elif math_ope == "-":
    print("Результат:", first_num - second_num)
elif math_ope == "*":
    print("Результат:", first_num * second_num)
elif math_ope == "/":
    if second_num != 0:
        print("Результат:", first_num / second_num)
    else:
        print("Помилка: ділення на нуль!")
else:
    print("Невірна математична дія!")
