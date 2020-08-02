#!/usr/bin/python3
#Author:pliu


def bitCountA(n):
    return bin(n).count("1")


if __name__ == '__main__':
    print(bitCountA(9))
    x = 218
    print(x&(-x) == x)
