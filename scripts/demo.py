#!/usr/bin/env python

def check_nums(n):
    for i in range(n):
        num=int(input("Enter: "))
        if num%2==0:
            print("even")
        else:
            print("not even")
        n -=1
        
        
def check_numbers(n):
    if n==0:
        return "Done"
    else:
        number=int(input("Enter number: "))
        if number%2==0:
            print("even")
        else:
            print("not even")
        check_numbers(n-1)
        
check_numbers(5)

