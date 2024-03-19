#!/bin/usr/python3
def multiple_returns(sentence):
    for i in sentence:
        length = len(sentence)
        if length == 0:
            return length, None
        else:
            return length, sentence[0]
