def even_no(list):
    count = 0
    even_numbers = []
    for i in list:
        if i%2 == 0:
            even_numbers.append(i)
            count += 1
    print("Even numbers in the list are :",even_numbers)
    print("Total even numbers are :",count)


def odd_no(list):
    count = 0
    odd_numbers = []
    for i in list:
        if i%2 != 0:
            odd_numbers.append(i)
            count += 1
    print("Odd numbers in the list are :",odd_numbers)
    print("Total odd numbers are :",count)