# new_file = open('create_txt.txt', 'w+')

# for num in range(1, 11):
#     ...

# new_file.close()

# Com a funcçaõ with open abre e fecha o arquivo

with open('create_txt.txt', 'w+') as file:
    for num in range(1, 11):
        file.write(f'This is the line {str(num)}.\n')


"""
Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter).
For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.
"""


def sum_of_num(limit):
    total = 0
    for num in range(limit + 1):
        if num % 3 == 0 or num % 5 == 0:
            print(num)
            total += num
    return total


print(sum_of_num(20))
