import math


def true_if_even(a):
    if a % 2 == 0:
        return True
    else:
        return False


def area(r):
    return r * r * math.pi


def greatest_value(my_numbers):
    my_numbers.sort()
    return my_numbers[-1]


def reverse_list(my_numbers):
    my_numbers.reverse()
    return my_numbers


def insert_list(my_numbers):
    my_numbers.insert(4, 3)
    my_numbers.sort()
    my_numbers.reverse()
    return my_numbers


def list_len(my_list):
    result_list = []
    for i in my_list:
        result_list += [len(i)]
    return result_list


def list_sum(my_numbers):
    res = 0
    for i in range(len(my_numbers)):
        res += my_numbers[i]
    return res

def list_flat(my_numbers):
    result_list = []
    for i in my_numbers:
        result_list += i
    return result_list


def main():
    list = [11, 12, 13, 14, 15, 16]
    print(insert_list(list))
    print(reverse_list(list))
    print(greatest_value(list))
    print(area(7))
    print(true_if_even(4))
    print(list_len(['abc', 'de', 'fghi']))
    print(sum([2,3,4]))
    print(list_flat([[3,8],[8,9,9],[1,2]]))


if __name__ == '__main__':
    main()
