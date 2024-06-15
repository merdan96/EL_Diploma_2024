#! /usr/bin/python

# input test list
input = [1,2,4,5,8,10,4,6,8,4,5]
test = 4
count = 0
for i in input:
    if i == test: count = count + 1

print("There are " + str(count) + " " + str(test) + "'s in the given list")