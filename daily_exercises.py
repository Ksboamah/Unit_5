def choose_upper_value():
    small = int(input("Count from (Pick a number)"))
    return small


def choose_lower_value(small):
    big = int(input("to (Pick a number)")) + 1
    if small > big:
        new_big = int(input("Your upper value is bigger than your lower value. Enter in appropriate values"))
        return new_big
    else:
        return big


def counter(small, big, new_big):

    else:
        for x in range(small, big, new_big):
            print(x)


def main():
    small = choose_upper_value()
    big = choose_lower_value(small)
    new big = if small > big or new_big:
                new_big = int(input("Your upper value is bigger than your lower value. Enter in appropriate values"))
                return new_big
    counter(small, big, new_big)


main()
