def choose_upper_value():
    small = int(input("Count from (Pick a number)"))
    return small


def choose_lower_value(small):
    big = int(input("to (Pick a number)")) + 1
    if small > big:
        y_n = input("Your lower value is larger than your Upper value. Do you wish to count down? Type (Yes)/(No)")
        if y_n == "Y":
            new_big = int(input("Your upper value is bigger than your lower value. Enter in appropriate values"))
            return new_big
        else:
            return big


def counter(small, big, new_big):
    for x in range(small, big or new_big, -1):
        print(x)


def main():
    small = choose_upper_value()
    big, new_big = choose_lower_value(small)
    counter(small, big, new_big)


main()
