import sys


def show_sales(from_number, by_number=0):
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        sale_list = ''
        if from_number > 0 and by_number == 0:
            lines = f.readlines()[from_number - 1:]
            for line in lines:
                sale_list += line
            return sale_list
        elif from_number > 0 and by_number != 0:
            lines = f.readlines()[from_number - 1:by_number]
            for line in lines:
                sale_list += line
            return sale_list
        for line in f:
            sale_list += line
        return sale_list


def main(*args):
    if not args:
        print(show_sales(0, 0))
        return
    elif len(args) == 1:
        print(show_sales(int(args[0])))
        return
    elif len(args) == 2:
        print(show_sales(int(args[0]), int(args[1])))
        return
    return


if __name__ == '__main__':
    cli_args = sys.argv[1:]
    exit(main(*cli_args))
