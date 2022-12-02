#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    my_list = sys.argv
    jb = len(my_list) - 1
    if jb == 1:
        print("{} argument:".format(int(jb)))
    elif jb == 0:
        print("{} arguments.".format(int(jb)))
    else:
        print("{} arguments:".format(int(jb)))
    for item in my_list:
        indx = my_list.index(item)
        if indx != 0:
            print("{}: {}".format(int(indx), item))
