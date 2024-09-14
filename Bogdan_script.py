print("Ця програмка виведе парні числа від 1 і до вашого числа включно")
numbers = int(input("Введіть число"))
for number in range(1, numbers + 1):
    if number % 2 == 0:
        print(number)