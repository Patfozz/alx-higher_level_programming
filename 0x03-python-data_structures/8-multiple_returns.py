#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        new_turple = (len(sentence), None)
    else:
        new_turple = (len(sentence), sentence[0])
    return(new_turple)
