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
    for x in range(13):
        print(num) * print(y)



def main():
    # small = choose_upper_value()
    # big = choose_lower_value(small)
    # print(big)
    # counter(small, big)
    # for x in range(10, 21):
    #     print(x)
    # for x in range(2, 41, 2):
    #     print(x)
    y == -1
    y =
    multiply()


main()
