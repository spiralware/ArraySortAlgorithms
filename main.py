from array_sort_algos import bubble_sort
from array_sort_algos import insertion_sort_immediate_change

def check_algo(func):
    input_file = open('input.txt')
    output_file = open('output.txt')

    ok = True
    while True:
        input_row = input_file.readline()
        output_row = output_file.readline()

        if input_row == '':
            break

        input_array = [int(i) for i in input_row.split()]
        output_array = [int(i) for i in output_row.split()]

        func(input_array)

        if input_array != output_array:
            ok = False
            break

    if ok:
        print('успех!')
    else:
        print('бунт на корабле!')

    input_file.close()
    output_file.close()

def main():
    check_algo(bubble_sort)
    check_algo(insertion_sort_immediate_change)
    

if __name__ == "__main__":
    main()