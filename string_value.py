import math
import os
import random
import re
import sys
def repeatedString(s, n):
    count = 0
    newstr = ''
    x = 0
    while x < n:
    	for j in s:
		newstr += s[j]
    for i in range(n - 1):
        if s[i] == 'a':
            count += 1
        else:
            pass
    return count
if __name__ == '__main__':

    s = 'aaaaadfsfdddddddddddaaaaaaaaaaadfedsfdsfdsfsddddddddddd'

    n = 15

    result = repeatedString(s, n)
    print(result)
