#!/usr/bin/python3
for i in range(97, 122):
    if  int (i) == 101 or int (i) == 113:
        continue
    print('{:c}'.format(i), end="")
