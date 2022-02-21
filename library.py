import random


def make_array(length, array_range = (0, 100)):
    array  = []
    for i in range(length):
        array += [random.randint(array_range[0], array_range[1])]
    return array

def make_float_array(length, array_range = (0, 100)):
    array  = []
    for i in range(length):
        array += [random.randint(array_range[0], array_range[1]) + random.random()]
    return array

def digit_input():
    list = []
    while True:
        console_str = input('Введите число. Если хотите закончить ввод, то нажмите q: ')
        if console_str == 'q':
            break  
        try:                                         
            list += [int(console_str)]
        except ValueError:                     
            print('"' + console_str + '"' + ' - не является числом')
    return list


def clean_sub_str(str, sub_str):
    tr = str.split()
    [tr.remove(word) for word in tr[:] if sub_str in word]
    return " ".join(tr)  


    

