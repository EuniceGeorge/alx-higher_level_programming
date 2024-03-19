#!/usr/bin/python3
def multiple_returns(sentence):
    string = []
    length = len(sentence)
    if length == 0:
        string.append(None)
        value = length, string[0]
        return (value)
    else:
        for i in sentence:
            string.append(i)
            value = length, string[0]
            return (value)
