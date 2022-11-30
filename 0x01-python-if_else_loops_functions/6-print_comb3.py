#!/usr/bin/python3
for i in range(0, 100):
    for s in range(9):
        if  i == s or s == i:
            print("{:02d}".format(i,s), end=", ")
