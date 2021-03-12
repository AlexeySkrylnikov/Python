rate = [7, 5, 3, 3, 2]

number = int(input('Введите число: '))
while number != 000:
    for element in range(len(rate)):
        if rate[element] == number:
            rate.insert(element+1, number)
            break
        elif rate[0] < number:
            rate.insert(0, number)
        elif rate[-1] > number:
            rate.append(number)
        elif not rate[element] <= number and rate[element + 1] < number:
            rate.insert(element + 1, number)
            break
    print(rate)
    number = int(input('Введите число: '))
