def add_two_numbers() -> int:
    str=input()
    str_nums=str.split(',')
    map_nums=map(int,str_nums)
    sums=0
    for num in map_nums:
        sums+=num
    return sums


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
