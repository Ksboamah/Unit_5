import random


def choose_upper_value():
    small = int(input("Count from (Pick a number)"))
    return small


def choose_lower_value(small):
    big = int(input("to (Pick a number)"))
    if small > big:
        y_n = input("Your lower value is larger than your Upper value. Do you wish to count down? Type (Yes)/(No)")
        if y_n == "Y":
            big = int(input("Your upper value is bigger than your lower value. Enter in appropriate values"))
            return big
        else:
            return big


def counter(small, big):
    for x in range(small, big, -1):
        print(x)


def multiply():
    num = int(input("Pick an integer"))
    return num


def main():
    # small = choose_upper_value()
    # big = choose_lower_value(small)
    # print(big)
    # counter(small, big)
    # for x in range(10, 21):
    #     print(x)
    # for x in range(2, 41, 2):
    #     print(x)
    # y = -1
    # y += 1
    # num = multiply()
    # for x in range(13):
    #     print(num, "*", y, "=", num * y)
    #     y += 1
    # even = 0
    # odd = 0
    # for x in range(10):
    #     rando = random.randint(1, 100)
    #     if rando % 2 == 0:
    #         even = even + rando
    #     if rando % 2 == 1:
    #         odd = odd + rando
    # print(odd)
    # print(even)
    # three = 0
    # five = 0
    # for x in range(1000):
    #     if x % 3 == 0:
    #         three = three + x
    #     if x % 5 == 0:
    #         five = five + x
    # print(three + five)
    size = int(input("How big do you want your triangle to be? (Enter in integer)"))
    for x in range(size):
        print("* " * (x + 1))


main()
