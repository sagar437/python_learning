#!/usr/bin/python

ar = [2,3,3,1]
count = 0
max_height = int(max(ar))
print(max_height)
for num in ar:
        if num == max_height:
            count = count + 1
print(count)
