#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    print("{:d} + {:d} = {:d}".format(a, add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, div(a, b)))
