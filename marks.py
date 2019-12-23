#!/usr/bin/env python3

# Created by Marwan Mashaly
# Created on December 2019
# This program finds the average mark from numbers given

import math


def average(mark_list):
    # This function finds the average

    total = 0

    for single_element in mark_list:
        total = total + single_element
    final = total / len(mark_list)
    final = round(final)
    return final


def main():
    # This function gets input from user

    mark_list = []
    mark = None

    while True:
        mark = input("Enter the mark of the student: ")
        if mark == "-1":
            break
        try:
            mark = float(mark)
        except Exception:
            print("Invalid Mark")
            return

        if mark >= 0 and mark <= 100:
            mark_list.append(mark)
    calc_average = average(mark_list)

    # Output
    print("")
    print(" the average of the marks is: {}".format(calc_average))


if __name__ == "__main__":
    main()
