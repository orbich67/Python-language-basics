import sys


def main_agr(*args):
    if not args:
        return
    for idx in range(len(args)):
        with open('bakery.csv', 'a', encoding='utf-8') as f:
            f.write(f'{args[idx]}\n')
    return


if __name__ == '__main__':
    cli_args = sys.argv[1:]
    exit(main_agr(*cli_args))
