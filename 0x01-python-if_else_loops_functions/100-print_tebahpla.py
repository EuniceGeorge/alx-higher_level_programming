#!/usr/bin/python3
for num in range(-122, -96):
    num *= -1
    if num % 2 == 1:
        num -= 32
    print('{:s}'.format(chr(num)), end ='')
