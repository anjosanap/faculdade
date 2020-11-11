def main():
    number = input()
    calculate(number)


def calculate(number):
    sum = 0
    for n in number:
        sum += int(n)
    print(sum)


main()
