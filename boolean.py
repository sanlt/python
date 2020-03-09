import math


def true_if_even(a):
    if a % 2 == 0:
        return True
    else:
        return False


def area(r):
    return r * r * math.pi


def greatest_value(myNumbers):
    myNumbers.sort() 
    return myNumbers[-1]


def reverse_list(myNumbers):
    myNumbers.reverse()
    return myNumbers


def insert_list(myNumbers):
    myNumbers.insert(4, 3)
    myNumbers.sort()
    myNumbers.reverse()
    return myNumbers


def main():
    list = [11, 12, 13, 14, 15, 16]
    print(insert_list(list))
    print(reverse_list(list))
    print(greatest_value(list))
    print(area(7))
    print(true_if_even(4))


if __name__ == '__main__':
    main()
