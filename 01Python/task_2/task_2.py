#! /usr/bin/python

input = input("Please enter a character : ")
if len(input) == 1:
    flag = str.lower(input) in list("aeiou")
    print("The character " + input + " is a vowel ? " + str(flag))