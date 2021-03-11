import utils
import sys


def main_agr(args):
    for idx in range(len(args)):
        print(utils.currency_rates(args[idx]))


main_agr(sys.argv[1:])
