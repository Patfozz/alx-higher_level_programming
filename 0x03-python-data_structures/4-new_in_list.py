#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if not my_list:
        pass
    if idx < 0 or idx > (len(my_list) - 1):
        return(my_list)
    else:
        newlist = []
        newlist.extend(my_list)
        newlist[idx] = element
        return(newlist)
