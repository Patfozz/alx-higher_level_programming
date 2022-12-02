#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    my_list = (sys.argv)
    a = []
    for item in my_list:
        if my_list.index(item) != 0:
            a.append((item))
    b = [int(x) for x in a]
    print("{}".format(sum(b)))
