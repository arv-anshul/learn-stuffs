import math
import os


def print_cwd():
    print(os.getcwd())


def add(*nums: int):
    return sum(nums)


def calc_pow(num: float, pow: int = 2):
    return math.pow(num, pow)


if __name__ == "__main__":
    print_cwd()
    add(14, 15, 141, 13)
    add(23, 24)
    d_comp = r"\d"
